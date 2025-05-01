import numpy as np
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