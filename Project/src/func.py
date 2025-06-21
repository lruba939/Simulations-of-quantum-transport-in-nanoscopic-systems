import numpy as np
import os
from scipy.optimize import differential_evolution, curve_fit

from src.eq import conductance
from src.params import *
from src.units import *

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
    
    res = differential_evolution(loss, bounds, tol=1e-6)
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