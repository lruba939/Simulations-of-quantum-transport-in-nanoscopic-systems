from src.params import *
from src.eq import ewe
from src.quantum_eq import *
from visualization.plotter import *


def main():
    # p = SimParams()
    # p.showParams()
    
    # S_mat = np.zeros((p.N, p.N))
    # dupa = ewe(S_mat, H_kl)
    # map_plotter(dupa, cm=cm_viridis, xborder=81, yborder=81)
    
    # print(eigenvalues_of_energy())
    
    phi = wavfun(1)
    map_plotter(phi, cm=cm_jet, xborder=4, yborder=4)

if __name__ == "__main__":
    main()