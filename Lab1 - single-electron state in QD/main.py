from src.params import *
from src.eq import ewe
from src.quantum_eq import *
from visualization.plotter import *


def main():
    p = SimParams()
    p.showParams()
    
    ## Checks sections
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
    
    ## Task no 1
    gaussians = [vec2mat(k) for k in [0,8,9]]
    map_grid_plotter(gaussians, n=1, m=3, xborder=4, yborder=4, cm=cm_jet)
    
    ## Task no 2
    wavefunctions = [np.abs(wavfun(k))**2 for k in range(6)]
    map_grid_plotter(wavefunctions, n=2, m=3, xborder=4, yborder=4, cm=cm_jet)

    ## Task no 3
    energies_vec = []
    styles = ['-' for _ in range(10)]

    omegax_range = np.arange(20, 501, 10)
    for omegax in omegax_range:
        p.omegax = omegax/p.hartree_to_meV
        energies_vec.append(eigenvalues_of_energy(10))

    energies_vec = np.array(energies_vec)
    ydata = [energies_vec[:,i] for i in range(10)]

    for num in [1, 2, 3]:
        ene_anal = []
        ene_anal = [(omegax*(num+0.5)+p.omegay*p.hartree_to_meV*0.5) for omegax in omegax_range]
        ydata.append(ene_anal)
        styles.append(':')
            
    multi_line_plotter_same_axes([omegax_range/1000 for _ in range(13)], ydata, cm2c(cm_tab10, 10), xlabel=r"$\omega_x$ [eV]", linestyles=styles)

    ## Task no 4
    p.reset_to_defaults()
    
    p.omegay = 350/p.hartree_to_meV
    wavefunctions = [np.abs(wavfun(k))**2 for k in range(6)]
    map_grid_plotter(wavefunctions, n=2, m=3, xborder=4, yborder=4, cm=cm_jet)

if __name__ == "__main__":
    main()