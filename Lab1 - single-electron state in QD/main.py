from src.params import *
from src.eq import ewe
from src.quantum_eq import *
from visualization.plotter import *


def main():
    p = SimParams()
    p.showParams()
    
    # S_mat = np.zeros((p.N, p.N))
    # S_mat = ewe(S_mat, S_kl)
    # map_plotter(S_mat, cm=cm_viridis, xborder=81, yborder=81, title="S matrix")
    
    # K_mat = np.zeros((p.N, p.N))
    # K_mat = ewe(K_mat, K_kl)
    # map_plotter(K_mat, cm=cm_viridis, xborder=81, yborder=81, title="K matrix")
    
    # V_mat = np.zeros((p.N, p.N))
    # V_mat = ewe(V_mat, V_kl)
    # map_plotter(V_mat, cm=cm_viridis, xborder=81, yborder=81, title="V matrix")
    
    # H_mat = np.zeros((p.N, p.N))
    # H_mat = ewe(H_mat, H_kl)
    # map_plotter(H_mat, cm=cm_viridis, xborder=81, yborder=81, title="H matrix")
    
    # print(eigenvalues_of_energy())
    
    # gaussians = [vec2mat(k) for k in [0,8,9]]
    # map_grid_plotter(gaussians, n=1, m=3, xborder=4, yborder=4, cm=cm_jet)
    
    # wavefunctions = [np.abs(wavfun(k))**2 for k in range(6)]
    # map_grid_plotter(wavefunctions, n=2, m=3, xborder=4, yborder=4, cm=cm_jet)


if __name__ == "__main__":
    main()