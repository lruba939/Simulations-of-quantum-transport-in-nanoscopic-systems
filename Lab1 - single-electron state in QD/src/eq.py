import numpy as np
from src.params import *

# Get parameters
p = SimParams() # Singleton of parameters

def calc_xy_k(xy, k):
    if xy == 'x':
        return -1. * p.a + p.dx * int(k/p.n)
    if xy == 'y':
        return -1. * p.a + p.dx * int(k%p.n)
    else:
        print("\nIncorrect calc_xy_k() call!\nUse 'x' or 'y'.\n")
        return None

def gaussian_fun_val(x, y, k):
    xk = p.xk[k]
    yk = p.yk[k]
    
    part1 = (np.pi * p.alpha('x')) **(-1/4)
    part2 = np.exp( - (x - xk)**2 / (2*p.alpha('x')) )
    part3 = (np.pi * p.alpha('y'))**(-1/4)
    part4 = np.exp( - (y - yk)**2 / (2*p.alpha('y')) )

    return part1 * part2 * part3 * part4

def gaussian_val_vec(k):
    gauss_vec = np.array([])
    for i in range(p.dim):
        y = -1. * p.a + p.dx_denser * i
        for j in range(p.dim):
            x = -1. * p.a + p.dx_denser * j
            gauss_val = gaussian_fun_val(x,y,k)
            gauss_vec = np.concatenate((gauss_vec, gauss_val), axis=None)
    
    return gauss_vec

def vec2mat(k=None, vector=None):
    if vector != None:
        if isinstance(vector, np.ndarray):
            return vector.reshape((p.dim, p.dim))
        else:
            print("\n\nError! Wrong type, you should pass a 'np.ndarray'.\n")
    if k != None:    
        gauss_val = gaussian_val_vec(k)    
        return gauss_val.reshape((p.dim, p.dim))
    else:
        print("\n\nError! Wrong parameters in gaussian_matrix().\n")

def ewe(matrix, function):  # each with each
    for k in range(p.N):
        for l in range(k, p.N): # because we know that matrix will be simetric
            val = function(k, l)
            
            matrix[k,l] = val
            matrix[l,k] = val
    
    return matrix