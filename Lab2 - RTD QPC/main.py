from src.params import *
from src.eq import *
from visualization.plotter import *

def main():
    p = SimParams()
    p.set_sys(1)
    p.showParams()
    
    line_plotter([i for i in range(p.N)], p.z, xlabel="N", ylabel="z")
    plt.show()
    line_plotter(p.z, p.U, xlabel="z", ylabel="U")
    plt.show()
    line_plotter(p.z, p.k, xlabel="z", ylabel="k")
    plt.show()
    
    # print(p.k)

    # Task 1
    E_arr = np.linspace(0.01, 1.0, 999)
    T = []
    R = []
    for newE in E_arr:
        p.set_E(newE)
        valT, valR = calc_T_R()
        T.append(valT)
        R.append(valR)
        
    line_plotter(E_arr, T, xlabel="E", ylabel="Trans")
    plt.show()
    line_plotter(E_arr, R, xlabel="E", ylabel="Refl")
    plt.show()

if __name__ == "__main__":
    main()