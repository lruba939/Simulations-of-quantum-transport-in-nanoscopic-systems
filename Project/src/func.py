import numpy as np
import os
from scipy.optimize import differential_evolution, curve_fit, dual_annealing

from src.eq import conductance
from src.params import *
from src.units import *
from visualization.plotter import *

p = SimParams()

def load_data(name, folder=p.Cu_dir):
    path = os.path.join(folder, name)
    data = np.loadtxt(path, delimiter=',')
    V, G = data[:,0], data[:,1]
    return V*1e-3, G

def global_guess(V, G):
    bounds = [
      (0, 5), # Z
      (0, 3e-3), # Delta
      (0, 1),     # P
      ]
    def loss(params):
        Z, D, P = params
        
        p.Z = Z
        p.Delta_val = units.eV2au(D)
        p.P = P
        
        Gmod = conductance(V)
        
        err = np.sum((Gmod - G)**2)
        
        print(f"Error val: {err}")
        
        return err
    
    # res = differential_evolution(loss, bounds, tol=0.01)
    res = dual_annealing(loss, bounds, maxiter=50)
    return res.x

def fit_KWANT(name, folder=p.Cu_dir):
    V, G = load_data(name, folder)
    # globalne zgadywanie parametrów
    Z0, D0, P0 = global_guess(V, G)
    print(f'Fit final: Z={Z0:.3f}, Δ={D0*1e3:.2f} mV, P={P0:.3f}')

    p.reset_to_defaults()
    p.Z = Z0; p.P = P0; p.Delta = D0; p.Delta_val = units.eV2au(D0);

    Vfit = np.linspace(V[0], V[-1], 200)
    Gfit = conductance(Vfit)
    
    return V, G, Gfit, Vfit

def plot_files(dir, figs_dir):
    os.makedirs(figs_dir, exist_ok=True)

    datas = [['# Name', 'Z', 'Delta', 'P']]

    for filename in os.listdir(dir):
        print(f"Processing file: {filename}")
        base_filename = os.path.splitext(filename)[0]

        V, G, Gfit, Vfit = fit_KWANT(filename, figs_dir)
    
        plot_fit(p, V, G, Vfit, Gfit, filename, dir, show=True, save=True)

        output_filename = f"{base_filename}.png"
        p.output_path = os.path.join(figs_dir, output_filename)

        print(f"Plot saved to: {p.output_path}")

        datas.append([filename, p.Z, p.Delta, p.P])

    save_file_path = os.path.join(figs_dir, f'{dir[-5:]}.dat')
    np.savetxt(save_file_path, datas, delimiter=',', fmt='%s')