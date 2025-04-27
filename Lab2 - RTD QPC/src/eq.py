import numpy as np
from src.params import *

p = SimParams()

def Mn11(k, kp, m, mp, z):
    part1 = 1 + (kp*m) / (k*mp)
    in_exp = (kp-k)*z
    part2 = np.exp(in_exp*1j)
    result = 1./2. * part1 * part2
    
    return result

def Mn12(k, kp, m, mp, z):
    part1 = 1 - (kp*m) / (k*mp)
    in_exp = (kp+k)*z
    part2 = np.exp(-1*in_exp*1j)
    result = 1./2. * part1 * part2
    
    return result

def Mn21(k, kp, m, mp, z):
    part1 = 1 - (kp*m) / (k*mp)
    in_exp = (kp+k)*z
    part2 = np.exp(in_exp*1j)
    result = 1./2. * part1 * part2
    
    return result

def Mn22(k, kp, m, mp, z):
    part1 = 1 + (kp*m) / (k*mp)
    in_exp = (kp-k)*z
    part2 = np.exp(-1*in_exp*1j)
    result = 1./2. * part1 * part2
    
    return result

def M1N(M):
    result = 1
    for i in range(p.N-1):
        k = p.k[i]
        kp = p.k[i+1]
        z = p.z[i]
        m = p.m[i]
        mp = p.m[i+1]
        val = M(k, kp, m, mp, z)
        result = result*val
    
    return result

def sqmodM1N(M):
    val = M1N(M)
    result = (np.abs(val))**2
    
    return result
    
def calc_T():
    part1 = np.abs(p.k[-1]) * p.m[0]
    part2 = np.abs(p.k[0]) * p.m[-1]
    part3 = sqmodM1N(Mn11)
    
    result = part1 / part2 / part3
    
    return result

def calc_R():
    part1 = sqmodM1N(Mn21)
    part2 = sqmodM1N(Mn11)
    
    # print(part1, "  ", part2)
    
    result = part1 / part2
    
    return result