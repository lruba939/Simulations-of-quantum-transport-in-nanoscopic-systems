import kwant
import numpy as np
import matplotlib.pyplot as plt
import types
from src.params import *
from src.units import *
from src.eq import *
from src.syst import *
from visualization.plotter import *

def main():
    p = SimParams()

    # ## Task 1
    # nw = types.SimpleNamespace(\
    #                     dx=nm2au(2),
    #                     L=int(100),
    #                     W=int(15),
    #                     m=0.014 
    #                     )

    # sys=make_system(nw)
    # kwant.plot(sys, site_color=lambda site: sys.hamiltonian(site,site), fig_size=(10,5), colorbar=False, show=False, num_lead_cells=2);
    # plt.tight_layout()
    # plt.savefig("priv/plots/sys1.png")
    # # plt.show()

    # momenta, energies = disperssion(nw, 0, .1, 200)
    # plt.figure(figsize=(6,6))
    # plt.plot(momenta, np.asarray(energies)/eV2au(1.0),'k-')
    # plt.tick_params(axis='both', which='major', labelsize=22)
    # plt.ylim((0,.2))  
    # plt.xlim((-0.5,.5))  
    # plt.xlabel("k [1/nm]",fontsize=22)
    # plt.ylabel("E [eV]",fontsize=22)
    # plt.tight_layout()
    # plt.savefig("priv/plots/disp1.png")
    # # plt.show()

    # energies, cond=conductance(nw, 0.2, 50)
    # plt.figure(figsize=(8,4))
    # plt.plot(energies, cond,'k-')
    # plt.tick_params(axis='both', which='major', labelsize=22)
    # plt.xlabel("E [eV]",fontsize=22)
    # plt.ylabel("G [2e^2/h]",fontsize=22)
    # plt.tight_layout()
    # plt.savefig("priv/plots/cond1.png")
    # # plt.show()
    
    # fig, axs = plt.subplots(2, 3, figsize=(20, 5), dpi = 300)
    # wave_function(nw, 0.03, 0, ax = axs[0, 0])
    # axs[0, 0].set_title("Energy = 30 meV", fontsize=22)
    # wave_function(nw, 0.05, 0, ax = axs[0, 1])
    # axs[0, 1].set_title("Energy = 50 meV", fontsize=22)
    # wave_function(nw, 0.1, 0, ax = axs[0, 2])
    # axs[0, 2].set_title("Energy = 100 meV", fontsize=22)
    # current(nw, 0.03, 0, 0, ax = axs[1, 0])
    # current(nw, 0.05, 0, 0, ax = axs[1, 1])
    # current(nw, 0.1, 0, 0, ax = axs[1, 2])
    # plt.tight_layout()
    # plt.savefig("priv/plots/wav1.png")
    # # plt.show()
    
    
    # ## Task 2    
    # p.B = units.T2au(2)
    # p.V0 = 0.
    
    # nw = types.SimpleNamespace(\
    #                     dx=nm2au(2),
    #                     L=int(100),
    #                     W=int(20),
    #                     m=0.014 
    #                     )

    # sys=make_system(nw)
    # kwant.plot(sys, site_color=lambda site: sys.hamiltonian(site,site), fig_size=(10,5), colorbar=False, show=False, num_lead_cells=2);
    # plt.tight_layout()
    # plt.savefig("priv/plots/sys2.png")
    # # plt.show()
    
    # moments, enes = disperssion(nw, 0, .1, 200)
    # plt.figure(figsize=(6,6))
    # plt.plot(moments, np.asarray(enes)/units.eV2au(1.0),'k-')
    # plt.tick_params(axis='both', which='major', labelsize=22)
    # plt.ylim((0,.2))
    # plt.xlim((-0.5,.5))
    # plt.xlabel("k [1/nm]",fontsize=22)
    # plt.ylabel("E [eV]",fontsize=22)
    # plt.tight_layout()
    # plt.savefig("priv/plots/disp2_1.png")
    # #plot.show()

    # nw = types.SimpleNamespace(\
    #                     dx=nm2au(2),
    #                     L=int(100),
    #                     W=int(50),
    #                     m=0.014 
    #                     )
    # moments, enes = disperssion(nw, 0, .1, 200)
    # plt.figure(figsize=(6,6))
    # plt.plot(moments, np.asarray(enes)/units.eV2au(1.0),'k-')
    # plt.tick_params(axis='both', which='major', labelsize=22)
    # plt.ylim((0,.2))
    # plt.xlim((-0.5,.5))
    # plt.xlabel("k [1/nm]",fontsize=22)
    # plt.ylabel("E [eV]",fontsize=22)
    # plt.tight_layout()
    # plt.savefig("priv/plots/disp2_2.png")
    # #plt.show()

    # ene, cond = conductance(nw, 0.1, 50)
    # plt.figure(figsize=(8,4))
    # plt.plot(ene, cond, color = "black")
    # plt.xlabel("E [eV]",fontsize=22)
    # plt.ylabel("G [2e^2/h]",fontsize=22)
    # plt.tight_layout()
    # plt.savefig("priv/plots/cond2_2")
    # #plt.show()

    # fig, ax = plt.subplots(1, 2, dpi = 300)
    # wave_function(nw, 1e-2, 0, ax = ax[0])
    # wave_function(nw, 1e-2, 1, ax = ax[1])
    # ax[0].set_xlabel("x [a.u.]",fontsize=22)
    # ax[0].set_ylabel("y [a.u.]",fontsize=22)
    # ax[1].set_xlabel("x [a.u.]",fontsize=22)
    # ax[1].set_ylabel("y [a.u.]",fontsize=22)
    # plt.tight_layout()
    # plt.savefig("priv/plots/wav2_2")
    # #plt.show()
    
    
    ## Task 3
    p.B = 0
    
    nw = types.SimpleNamespace(\
                        dx=nm2au(2),
                        L=int(50),
                        W=int(15),
                        m=0.014,
                        R1=nm2au(60),
                        R2=nm2au(120)
                        )
    sys = make_system(nw, is_ring=1)
    kwant.plot(sys, site_color=lambda site: sys.hamiltonian(site,site), fig_size=(10,5), colorbar=False, show=False, num_lead_cells=2);
    plt.tight_layout()
    plt.savefig("priv/plots/sys3.png")
    # plt.show()
    
    moments, enes = disperssion(nw, 0, .1, 200)
    plt.figure(figsize=(6,6))
    plt.plot(moments, np.asarray(enes)/eV2au(1.0),'k-')
    plt.tick_params(axis='both', which='major', labelsize=22)
    plt.ylim((0,.1))
    plt.xlim((-0.2,.2))
    plt.xlabel("k [1/nm]",fontsize=22)
    plt.ylabel("E [eV]",fontsize=22)
    plt.tight_layout()
    plt.savefig("priv/plots/disp3.png")
    # plt.show()
    
    B_arr = np.linspace(-10, 10, 40)
    up = []
    down = []
    ene = 0.10

    for B in B_arr:
        p.B = T2au(B)
        up.append(transmission(nw, ene, 1, 0, is_ring=1))
        down.append(transmission(nw, ene, 2, 0, is_ring=1))
        
    plt.figure(figsize=(8,4))
    plt.plot(B_arr, up, color = cm2c(cm_inferno, 10)[2])
    plt.plot(B_arr, down, color = cm2c(cm_inferno, 10)[6])
    plt.xlabel("Bz [T]",fontsize=22)
    plt.ylabel("G [2e^2/h]",fontsize=22)
    plt.tight_layout()
    plt.savefig("priv/plots/cond3.png")
    # plt.show()

if __name__ == "__main__":
    main()