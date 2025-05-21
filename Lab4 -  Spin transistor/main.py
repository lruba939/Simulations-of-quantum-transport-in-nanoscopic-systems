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

    ## Task 1
    
    p.alpha = 0.
    
    nw = types.SimpleNamespace(\
                        dx=nm2au(4),
                        L=nm2au(p.L),
                        W=nm2au(p.W),
                        m=p.m_eff,
                        mag_region_con = 0
                        )

    sys=make_system(nw)
    # kwant.plot(sys, fig_size=(10,5), colorbar=False, show=False, num_lead_cells=2);
    # plt.show()
    
    # momenta, energies = disperssion(nw, 0, .05, 200)
    # plt.figure(figsize=(4,4))
    # plt.plot(momenta, np.asarray(energies)/eV2au(1.0),'k-')
    # plt.tick_params(axis='both', which='major', labelsize=22)
    # # plt.ylim((0,.2))  
    # plt.xlim((-0.15,0.15))
    # plt.ylim((0.0, 0.04))
    # plt.xlabel("k [1/nm]",fontsize=22)
    # plt.ylabel("E [eV]",fontsize=22)
    # plt.tight_layout()
    # plt.savefig("priv/plots/disp1.png")
    # plt.show()
    
    # p.B_x = T2au(1)
    
    # momenta, energies = disperssion(nw, 0, .05, 200)
    # plt.figure(figsize=(4,4))
    # plt.plot(momenta, np.asarray(energies)/eV2au(1.0),'k-')
    # plt.tick_params(axis='both', which='major', labelsize=22)
    # # plt.ylim((0,.2))  
    # plt.xlim((-0.15,0.15))
    # plt.ylim((0.0, 0.05))
    # plt.xlabel("k [1/nm]",fontsize=22)
    # plt.ylabel("E [eV]",fontsize=22)
    # plt.tight_layout()
    # plt.savefig("priv/plots/disp2_1.png")
    # plt.show()

    # p.B_x = 0.
    # p.B_y = T2au(1.)
    
    # momenta, energies = disperssion(nw, 0, .05, 200)
    # plt.figure(figsize=(4,4))
    # plt.plot(momenta, np.asarray(energies)/eV2au(1.0),'k-')
    # plt.tick_params(axis='both', which='major', labelsize=22)
    # # plt.ylim((0,.2))  
    # plt.xlim((-0.15,0.15))
    # plt.ylim((0.0, 0.05))
    # plt.xlabel("k [1/nm]",fontsize=22)
    # plt.ylabel("E [eV]",fontsize=22)
    # plt.tight_layout()
    # plt.savefig("priv/plots/disp2_2.png")
    # plt.show()
    
    # p.B_y = 0.
    # p.B_z = T2au(1.)
    
    # momenta, energies = disperssion(nw, 0, .05, 200)
    # plt.figure(figsize=(4,4))
    # plt.plot(momenta, np.asarray(energies)/eV2au(1.0),'k-')
    # plt.tick_params(axis='both', which='major', labelsize=22)
    # # plt.ylim((0,.2))  
    # plt.xlim((-0.15,0.15))
    # plt.ylim((0.0, 0.05))
    # plt.xlabel("k [1/nm]",fontsize=22)
    # plt.ylabel("E [eV]",fontsize=22)
    # plt.tight_layout()
    # plt.savefig("priv/plots/disp2_3.png")
    # plt.show()

    # p.B_z = T2au(1.)
    # energies, cond=conductance(nw, 0.05, 50)
    # plt.figure(figsize=(8,4))
    # plt.plot(energies, cond,'k-')
    # plt.tick_params(axis='both', which='major', labelsize=22)
    # plt.xlabel("E [eV]",fontsize=22)
    # plt.ylabel("G [2e^2/h]",fontsize=22)
    # plt.tight_layout()
    # plt.savefig("priv/plots/cond1.png")
    # plt.show()
    
    # mag_region_vals = np.linspace(0, 1, 50)
    # transmittances = np.zeros((len(mag_region_vals), 4))
    
    # E = 0.005
    # p.B_z = T2au(0.1)
    
    # for idx, B in enumerate(mag_region_vals):
    #     nw = types.SimpleNamespace(\
    #                     dx=nm2au(4),
    #                     L=nm2au(p.L),
    #                     W=nm2au(p.W),
    #                     m=p.m_eff,
    #                     mag_region_con = 1,
    #                     mag_region = [0.2, 0.8],
    #                     mag_reg_dir = 'Y',
    #                     mag_region_val = T2au(B)
    #                     )
    #     t_upup = transmission_spins(nw, E, [1, 0], [1, 1])
    #     t_updown = transmission_spins(nw, E, [1, 0], [0, 1])
    #     t_downup = transmission_spins(nw, E, [1, 0], [1, 0])
    #     t_downdown = transmission_spins(nw, E, [1, 0], [0, 0])
    #     transmittances[idx, 0] = t_upup
    #     transmittances[idx, 1] = t_updown
    #     transmittances[idx, 2] = t_downup
    #     transmittances[idx, 3] = t_downdown
    
    # colors = cm2c(cmap=cm_inferno, c_numb=12)
    
    # line_plotter(mag_region_vals, transmittances[:,0], xlabel="B [T]", ylabel="Transmittance", color=colors[2], linestyle="-", label=r'T$_{up \rightarrow up}$')
    # plt.plot(mag_region_vals, transmittances[:,1], color=colors[4], linestyle='-', label=r'T$_{up \rightarrow down}$')
    # plt.plot(mag_region_vals, transmittances[:,2], color=colors[9], linestyle='--', label=r'T$_{down \rightarrow up}$')
    # plt.plot(mag_region_vals, transmittances[:,3], color=colors[7], linestyle='--', label=r'T$_{down \rightarrow down}$')
    # plt.legend(fontsize=14)
    # plt.tight_layout()
    # plt.savefig("priv/plots/trans1.png")
    # plt.show()
    
if __name__ == "__main__":
    main()