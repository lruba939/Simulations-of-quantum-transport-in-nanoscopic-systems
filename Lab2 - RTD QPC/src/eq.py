import numpy as np
from scipy import linalg
from src.params import *
from src.matrix import sqmodM1N

p = SimParams()

def calc_T_R():
    part1 = np.abs(p.k[-1]) * p.m[0]
    part2 = np.abs(p.k[0]) * p.m[-1]
    part3 = sqmodM1N()
    
    T = part1 / part2 / part3[0,0]

    R = part3[1,0] / part3[0,0]
    
    return T, R

def TsuEsaki(energies, bias):
    const_part = p.m_Ga * p.kB * p.T / (2. * np.pi**2)
    
    integral = 0.
    
    for ene in energies:
        p.set_sys(2, bias)
        p.set_E(ene)
        valT, _ = calc_T_R()
        
        ene = ene / p.hartree_to_eV
        up = 1 + np.exp( (p.mu_s-ene) / (p.kB*p.T) )
        down = 1 + np.exp( (p.mu_d-bias-ene) / (p.kB*p.T) )
        result = valT * np.log(up/down)
        
        integral = integral + result
    
    j = const_part * integral
    
    return j

def f(u, v):
    frac = 1 / (2*np.pi*p.eps)
    frac_inside = u*v / (p.d * np.sqrt( p.d**2 + u**2 + v**2 ))
    atan_result = np.arctan(frac_inside)
    result = frac * atan_result
    
    return result

# kradzione od owoj bo bardzo ladnie napisal
def V(x, y):
    l = p.L * p.g_start
    r = p.L * p.g_stop
    
    t = -p.g_space * p.W/2.
    b = -p.W * 2.
    
    f1 = f(x - l, y - b)
    f2 = f(x - l, t - y)
    f3 = f(r - x, y - b)
    f4 = f(r - x, t - y)
    
    g1 = p.Vg * (f1 + f2 + f3 + f4)

    b = p.g_space * p.W/2.
    t = p.W * 2.
    
    f1 = f(x - l, y - b)
    f2 = f(x - l, t - y)
    f3 = f(r - x, y - b)
    f4 = f(r - x, t - y)
    
    g2 = p.Vg * (f1 + f2 + f3 + f4)
    
    result = g1 + g2
    
    return result

def effectivePotential(N = 100, states = 5):
    xs = np.linspace(0, p.L, N)
    ys = np.linspace(-p.W/2., p.W/2., N)
    dy = ys[1] - ys[0]
    
    alpha = 1 / (2*p.m_Ga * dy**2)
    H = np.zeros(N, N)
    energies = []
    
    for (x_idx, x) in enumerate(xs):
        for (idx, y) in enumerate(ys):
            if(idx == 1):
                H[idx, idx] = 2 * alpha + V(x, y)
                H[idx, idx + 1] = -alpha
            if (idx == len(ys)):
                H[idx, idx] = 2 * alpha + V(x, y)
                H[idx, idx - 1] = -alpha
            else:
                H[idx, idx - 1] = -alpha
                H[idx, idx + 1] = -alpha
                H[idx, idx] = 2 * alpha + V(x, y)
        
        x_enes = linalg.eigh(H)[0][:states] * p.hartree_to_eV
        energies.append(x_enes)
        
    return energies

def calcConductance():
    N = 100
    energies = np.linspace(0.001 / p.hartree_to_eV, 200 / p.hartree_to_eV, N)
    conductances = []

    states = 5
    for idx, ene in enumerate(energies):
        conductances[idx] = getConductance(ene, states, 100)

    return energies, conductances

# def getConductance(energy, states, N):
#     eff_potential = effectivePotential(N=N, states=states)

#     x = np.linspace(0., p.L, N)
#     mass = [p.m_Ga for i in x]
#     temp_cond = 0.

#     for state in eachrow(eff_potential):
#         eff_pot = np.array(state)
#         k = genKvector(eff_pot, mass, energy)
#         qs = QuantumSystem(eff_pot, k, x, mass, energy, c, material, 0., qpc.length, 0.)
#         r = solve(qs)
#         temp_cond += r.transmittance

#     return temp_cond