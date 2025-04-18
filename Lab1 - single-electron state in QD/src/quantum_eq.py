from src.params import *
from src.eq import *
from scipy import linalg

p = SimParams()

def S_kl(k, l):
    xk = calc_xy_k('x', k)
    yk = calc_xy_k('y', k)
    xl = calc_xy_k('x', l)
    yl = calc_xy_k('y', l)
    
    frac1 = - (xk - xl)**2 / (4 * p.alpha('x'))
    frac2 = - (yk - yl)**2 / (4 * p.alpha('y'))
    result = np.exp(frac1 + frac2)

    return result

def K_kl(k, l):
    xk = calc_xy_k('x', k)
    yk = calc_xy_k('y', k)
    xl = calc_xy_k('x', l)
    yl = calc_xy_k('y', l)
    
    frac1 = ((xk - xl)**2 - 2*p.alpha('x')) / (4 * p.alpha('x')**2)
    frac2 = ((yk - yl)**2 - 2*p.alpha('y')) / (4 * p.alpha('y')**2)
    result = - 1 / (2*p.mstar) * (frac1 + frac2) * S_kl(k, l)

    return result

def V_kl(k, l):
    xk = calc_xy_k('x', k)
    yk = calc_xy_k('y', k)
    xl = calc_xy_k('x', l)
    yl = calc_xy_k('y', l)
    
    frac1 = ((xk + xl)**2 + 2*p.alpha('x')) / (4) * p.omegax**2
    frac2 = ((yk + yl)**2 + 2*p.alpha('y')) / (4) * p.omegay**2
    result = 1 / 2 * p.mstar * (frac1 + frac2) * S_kl(k, l)

    return result

def H_kl(k, l):
    return K_kl(k, l) + V_kl(k, l)

def eigenvalues_of_energy():
    H = np.zeros((p.N, p.N))
    S = np.zeros((p.N, p.N))
    
    H = ewe(H, H_kl)
    S = ewe(S, S_kl)
        
    return linalg.eigh(H, S)[0] * p.hartree_to_meV

def wavfun_coef():
    H = np.zeros((p.N, p.N))
    S = np.zeros((p.N, p.N))
    
    H = ewe(H, H_kl)
    S = ewe(S, S_kl)
    
    return linalg.eigh(H, S)[1]

def wavfun(wave_num):
    coef = wavfun_coef()

    wave = np.zeros((p.dim, p.dim))
    for i in range(p.dim):
        y = -1. * p.a + p.dx_denser * i
        
        for j in range(p.dim):
            x = -1. * p.a + p.dx_denser * j
            val = 0
            
            for k in range(p.N):
                for wl in range(wave_num):
                    val = val + coef[wl][k] * gaussian_fun_val(x, y, k)
            wave[i][j] = val
            
    return wave