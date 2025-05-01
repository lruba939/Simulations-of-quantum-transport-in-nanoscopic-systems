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

if __name__ == "__main__":
    main()