from src.params import *
from src.eq import *
from visualization.plotter import *

def main():
    p = SimParams()
    p.set_sys(1)
    p.showParams()
    
    # print(p.k)

    # Task 1
    E_arr = np.linspace(0.01, 1.0, 999)
    T = []
    R = []
    for newE in E_arr:
        # print(newE,"\n")
        p.set_E(newE)
        T.append(calc_T())
        R.append(calc_R())
        
    line_plotter(E_arr, T, xlabel="E", ylabel="Trans")
    plt.show()
    line_plotter(E_arr, R, xlabel="E", ylabel="Refl")
    plt.show()

if __name__ == "__main__":
    main()