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