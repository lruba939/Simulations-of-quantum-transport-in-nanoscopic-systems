from src.params import *
from src.eq import *
from visualization.plotter import *

def main():
    p = SimParams()
    p.showParams()
    
    # line_plotter([i for i in range(p.N)], p.z, xlabel="N", ylabel="z")
    # plt.show()
    # line_plotter(p.z, p.U, xlabel="z", ylabel="U")
    # plt.show()
    # line_plotter(p.z, p.m, xlabel="z", ylabel="m")
    # plt.show()
    # line_plotter(p.z, p.k, xlabel="z", ylabel="k")
    # plt.show()
    
    # print(p.k)

    # # Task 1a
    # p.m_Al = p.m_Ga
    # p.set_sys(1)
    # E_arr = np.linspace(0.01, 1.0, 999)
    # T = []
    # R = []
    # for newE in E_arr:
    #     p.set_E(newE)
    #     valT, valR = calc_T_R()
    #     T.append(valT)
    #     R.append(valR)
    # line_plotter(E_arr, T, xlabel="E", ylabel="", label="Transmittance", color=c_twilight[3])
    # plt.plot(E_arr, R, label="Reflectance", color=c_twilight[0])
    # plt.plot(E_arr, np.array(R)+np.array(T), linestyle=":", label="T+R", color=c_twilight[2])
    # plt.legend(loc="best")
    # plt.show()

    # # Task 1b
    # p.reset_to_defaults()
    # p.set_sys(1)
    # T = []
    # R = []
    # for newE in E_arr:
    #     p.set_E(newE)
    #     valT, valR = calc_T_R()
    #     T.append(valT)
    #     R.append(valR)
    # line_plotter(E_arr, T, xlabel="E", ylabel="", label="Transmittance", color=c_twilight[3])
    # plt.plot(E_arr, R, label="Reflectance", color=c_twilight[0])
    # plt.plot(E_arr, np.array(R)+np.array(T), linestyle=":", label="T+R", color=c_twilight[2])
    # plt.legend(loc="best")
    # plt.show()

    # # Task 2a
    # p.set_sys(2)
    # T = []
    # R = []
    # for newE in E_arr:
    #     p.set_E(newE)
    #     valT, valR = calc_T_R()
    #     T.append(valT)
    #     R.append(valR)
    # line_plotter(E_arr, T, xlabel="E", ylabel="", label="Transmittance", color=c_twilight[3])
    # plt.plot(E_arr, R, label="Reflectance", color=c_twilight[0])
    # plt.plot(E_arr, np.array(R)+np.array(T), linestyle=":", label="T+R", color=c_twilight[2])
    # plt.legend(loc="best")
    # plt.show()
    
    # # Task 2a
    # bias = 50e-3/p.hartree_to_eV
    # p.set_sys(2, bias)
    # line_plotter(p.z*p.bohr_radius, p.U*p.hartree_to_eV, xlabel="z", ylabel="U")
    # plt.show()
    
    # p.reset_to_defaults()
    # E_arr = np.linspace(1e-6, 87e-3*2, 1000)
    # j_arr = []
    # biases = np.linspace(1e-6, 0.5, 200)/p.hartree_to_eV
    
    # for bias in biases:
    #     print(int(bias/biases[-1]*100), "%\n")
    #     j = TsuEsaki(E_arr, bias)
    #     j_arr.append(j)
        
    # line_plotter(biases*p.hartree_to_eV*1e3, j_arr, xlabel="Bias [meV]", ylabel="j", color=c_twilight[0])
    # plt.show()
    
    # Task 3
    
    N = 100
    
    xs = np.linspace(0, p.L, N)
    ys = np.linspace(-p.W / 2., p.W / 2., N)

    Vmap = np.zeros((N,N))

    for x_idx, x in enumerate(xs):
        for y_idx, y in enumerate(ys):
            Vmap[y_idx, x_idx] = V(x,y) * p.hartree_to_eV

    map_plotter(Vmap, cm=cm_viridis, xborder=50, yborder=25)
    plt.show()
    
    p.reset_to_defaults()
    
    xs, energies = effectivePotential()
    xs = xs.T*p.bohr_radius
    energies = np.array(energies).T * p.hartree_to_eV
    
    multi_line_plotter_same_axes([xs[:] for i in range(5)], energies, xlabel="x [nm]", ylabel=r"E$_\text{n}$(x) [eV]", colors=cm2c(cm_viridis, 8))
    
    ene_con, con = calcConductance()
    
    line_plotter(ene_con, con, xlabel="E [eV]", ylabel=r"G [2e$^2$/h]")
    plt.show()
    
    p.reset_to_defaults()
    
    E1 = 0.05
    E2 = 0.1

    voltages = np.linspace(0, 25, 100)
    cond_e1 = []
    cond_e2 = []
    nstates = 5
    
    for (idx, vgate) in enumerate(voltages):
        p.Vg = vgate / p.hartree_to_eV
        ce1 = getConductance(E1, nstates, 100)
        ce2 = getConductance(E2, nstates, 100)
        cond_e1.append(ce1)
        cond_e2.append(ce2)
        
    multi_line_plotter_same_axes([voltages, voltages], [cond_e1, cond_e2], xlabel=r"V$_\text{g}$ [eV]", ylabel="G [2e$^2$/h]")

if __name__ == "__main__":
    main()