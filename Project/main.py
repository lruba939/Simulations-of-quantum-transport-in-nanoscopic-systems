import kwant
import numpy as np
import os
import matplotlib.pyplot as plt
from src.params import *
from src.units import *
from src.eq import *
from src.syst import *
from visualization.plotter import *

def main():
    p = SimParams()
    
    # p.showParams()

    # sys=make_system()
    # kwant.plot(sys, fig_size=(10,5), colorbar=False, show=False, num_lead_cells=2);
    # plt.show()
    
    ## Tests
    # x = np.arange(0, 1250, 1)*p.dx
    # delta = []
    # for xi in x:
    #     delta.append(p.delta_func(xi))
    # plt.plot(x, delta)
    # plt.show()
    
    # energies = np.linspace(0, 0.5e-3, 100)

    # R_ee = []
    # R_he = []
    # T = []

    # for E in energies:
    #     Ree, Rhe = reflection_coeffs(E)
    #     T_val = transmission(E) / 2
    #     R_ee.append(Ree)
    #     R_he.append(Rhe)
    #     T.append(T_val)

    # plt.plot(energies*1e3, R_ee, label="$R_{ee}$")
    # plt.plot(energies*1e3, R_he, label="$R_{he}$")
    # plt.plot(energies*1e3, T, label="$T$")
    # plt.xlabel("E [meV]")
    # plt.ylabel("Value")
    # plt.legend(loc='best')
    # plt.show()

    ## Final test
    
    # for Z in [0.0, 0.5, 1.0, 1.5]:
    #     p.Z = Z
    #     G = []
    #     for E in energies:
    #         Ree, Rhe = reflection_coeffs(E)
    #         G_val = 1 - Ree + Rhe
    #         G.append(G_val)
    #     plt.plot(energies.T*1e3, G, label=f"Z = {Z}")

    # plt.xlabel("E [meV]")
    # plt.ylabel("Conductance [2e²/h]")
    # plt.xlim([0.0,0.5])
    # plt.legend(loc="best")
    # plt.show()
    
    # p.reset_to_defaults()
    
    # for P in [0.0, 0.5, 0.8, 0.99]:
    #     p.P = P
    #     G = []
    #     for E in energies:
    #         Ree, Rhe = reflection_coeffs(E)
    #         G_val = 1 - Ree + Rhe
    #         G.append(G_val)
    #     plt.plot(energies.T*1e3, G, label=f"P = {P}")

    # plt.xlabel("E [meV]")
    # plt.ylabel("Conductance [2e²/h]")
    # plt.xlim([0.1,0.5])
    # plt.legend(loc="best")
    # plt.show()
    
        
if __name__ == "__main__":
    main()