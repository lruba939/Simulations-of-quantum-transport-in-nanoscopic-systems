import numpy as np
from src.params import *

p = SimParams()

def _Mn11(k, kp, m, mp, z):
    part1 = 1 + (kp*m) / (k*mp)
    in_exp = (kp-k)*z
    part2 = np.exp(in_exp*1j)
    m11 = 1./2. * part1 * part2
    
    return m11

def _Mn12(k, kp, m, mp, z):
    part1 = 1 - (kp*m) / (k*mp)
    in_exp = (kp+k)*z
    part2 = np.exp(-1*in_exp*1j)
    m12 = 1./2. * part1 * part2
    
    return m12

def _Mn21(k, kp, m, mp, z):
    part1 = 1 - (kp*m) / (k*mp)
    in_exp = (kp+k)*z
    part2 = np.exp(in_exp*1j)
    m21 = 1./2. * part1 * part2
    
    return m21

def _Mn22(k, kp, m, mp, z):
    part1 = 1 + (kp*m) / (k*mp)
    in_exp = (kp-k)*z
    part2 = np.exp(-1*in_exp*1j)
    m22 = 1./2. * part1 * part2
    
    return m22

def _iMatrix(i):
    k = p.k[i]
    kp = p.k[i+1]
    z = p.z[i]
    m = p.m[i]
    mp = p.m[i+1]
    
    m11 = _Mn11(k, kp, m, mp, z)
    m12 = _Mn12(k, kp, m, mp, z)
    m21 = _Mn21(k, kp, m, mp, z)
    m22 = _Mn22(k, kp, m, mp, z)
    
    Mi = np.array([[m11, m12],
                   [m21, m22]])

    return Mi

def _M1N():
    MN = np.array([[1, 1],
                  [1, 1]])
    for i in range(p.N-1):
        Mi = _iMatrix(i)
        Mnext = MN @ Mi # Matrix multiplication (same as np.matmul())
        MN = Mnext
    
    return MN

def sqmodM1N():
    MN = _M1N()
    M = (np.abs(MN))**2
    
    return M