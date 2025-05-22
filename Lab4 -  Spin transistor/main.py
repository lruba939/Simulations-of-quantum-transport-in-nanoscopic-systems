import kwant
import numpy as np
import os
import matplotlib.pyplot as plt
import types
from src.params import *
from src.units import *
from src.eq import *
from src.syst import *
from visualization.plotter import *

def main():
    p = SimParams()

    #### Task 1
    
    ## Task 1.1
    
    # p.alpha = 0.
    
    # nw = types.SimpleNamespace(\
    #                     dx=nm2au(4),
    #                     L=nm2au(p.L),
    #                     W=nm2au(p.W),
    #                     m=p.m_eff,
    #                     region_con = 0
    #                     )

    # sys=make_system(nw)
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
    
    ## Task 1.2
    
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
    
    ## Task 1.3

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
    
    ## Task 1.4
    
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
    #                     region_con = 1,
    #                     region = [0.2, 0.8],
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
    
    ## Task 1.5 and 1.6
    
    # p.B_z = T2au(0.1)
    # E = 0.005
    # p.alpha = 0.
    
    # nw = types.SimpleNamespace(\
    #                     dx=nm2au(4),
    #                     L=nm2au(p.L),
    #                     W=nm2au(p.W),
    #                     m=p.m_eff,
    #                     region_con = 1,
    #                     region = [0.2, 0.8],
    #                     mag_reg_dir = 'Y',
    #                     mag_region_val = T2au(0.6)
    #                     )
    
    # den_up = np.matrix([[1,0],
    #                     [0,0]])
    # den_down = np.matrix([[0,0],
    #                     [0,1]])
    # # den_both = np.matrix([[1,0],
    # #                     [0,1]])    
    
    # sys=make_system(nw)
    
    # wave_f=kwant.wave_function(sys, eV2au(E))(0)
    
    # density_up_op = kwant.operator.Density(sys, den_up)
    # density_down_op = kwant.operator.Density(sys,den_down)
    
    # density_up_map = density_up_op(wave_f[0])
    # density_down_map = density_down_op(wave_f[0])

    # fig, ax = plt.subplots(2, 1, figsize=(10,3))
    # kwant.plotter.map(sys, density_up_map, cmap=cm_inferno, ax=ax[0])
    # kwant.plotter.map(sys, density_down_map, cmap=cm_inferno, ax=ax[1])
    # ax[0].set_title("Spin up")
    # ax[1].set_title("Spin down")
    # plt.tight_layout()
    # plt.savefig("priv/plots/spin1_1.png", dpi=150)
    # plt.show()
    
    # density_x = kwant.operator.Density(sys, p.sigma_x)
    # density_y = kwant.operator.Density(sys, p.sigma_y)
    # density_z = kwant.operator.Density(sys, p.sigma_z)
    
    # density_x_map = density_x(wave_f[0])
    # density_y_map = density_y(wave_f[0])
    # density_z_map = density_z(wave_f[0])

    # fig, ax = plt.subplots(3, 1, figsize=(10,5))
    # kwant.plotter.map(sys, density_x_map, cmap=cm_inferno, ax=ax[0])
    # kwant.plotter.map(sys, density_y_map, cmap=cm_inferno, ax=ax[1])
    # kwant.plotter.map(sys, density_z_map, cmap=cm_inferno, ax=ax[2])
    # ax[0].set_title(r"Spin s$_x$")
    # ax[1].set_title(r"Spin s$_y$")
    # ax[2].set_title(r"Spin s$_z$")
    # plt.tight_layout()
    # plt.savefig("priv/plots/spin1_2.png", dpi=150)
    # plt.show()
    
    #### Task 2
    
    # Task 2.1
    
    p.reset_to_defaults()
    
    p.Delta_x = 4
    p.L = int(800 / p.Delta_x)
    p.alpha = nm2au(eV2au(50e-3))
    
    nw = types.SimpleNamespace(\
                        dx=nm2au(4),
                        L=nm2au(p.L),
                        W=nm2au(p.W),
                        m=p.m_eff,
                        region_con = 0
                        )

    # sys=make_system(nw)
    # kwant.plot(sys, fig_size=(10,5), colorbar=False, show=False, num_lead_cells=2);
    # plt.show()
    
    # momenta, energies = disperssion(nw, 0, .05, 500)
    # plt.figure(figsize=(4,4))
    # plt.plot(momenta, np.asarray(energies)/eV2au(1.0),'k-')
    # plt.tick_params(axis='both', which='major', labelsize=22)
    # # plt.ylim((0,.2))  
    # plt.xlim((-0.15,0.15))
    # plt.ylim((0.0, 0.05))
    # plt.xlabel("k [1/nm]",fontsize=22)
    # plt.ylabel("E [eV]",fontsize=22)
    # plt.tight_layout()
    # plt.savefig("priv/plots/disp2.png")
    # plt.show()
    
    ## Task 2.2
    
    # energies, cond=conductance(nw, 0.05, 50)
    # plt.figure(figsize=(8,4))
    # plt.plot(energies, cond,'k-')
    # plt.tick_params(axis='both', which='major', labelsize=22)
    # plt.xlabel("E [eV]",fontsize=22)
    # plt.ylabel("G [2e^2/h]",fontsize=22)
    # plt.tight_layout()
    # plt.savefig("priv/plots/cond2.png")
    # plt.show()
    
    # # Task 2.3
    
    # alpha_region_vals = np.linspace(0, 50e-3, 20)
    # transmittances = np.zeros((len(alpha_region_vals), 4))
    
    # E = 0.005

    # for idx, alpha in enumerate(alpha_region_vals):
    #     p.alpha = nm2au(eV2au(alpha))
        
    #     nw = types.SimpleNamespace(\
    #                     dx=nm2au(4),
    #                     L=nm2au(p.L),
    #                     W=nm2au(p.W),
    #                     m=p.m_eff,
    #                     region_con = 2,
    #                     region = [0.2, 0.8]
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
    
    # line_plotter(alpha_region_vals, transmittances[:,0], xlabel=r"$\alpha$ [meV $\cdot$ nm]", ylabel="Transmittance", color=colors[2], linestyle="-", label=r'T$_{up \rightarrow up}$')
    # plt.plot(alpha_region_vals, transmittances[:,1], color=colors[4], linestyle='-', label=r'T$_{up \rightarrow down}$')
    # plt.plot(alpha_region_vals, transmittances[:,2], color=colors[9], linestyle='--', label=r'T$_{down \rightarrow up}$')
    # plt.plot(alpha_region_vals, transmittances[:,3], color=colors[7], linestyle='--', label=r'T$_{down \rightarrow down}$')
    # plt.legend(fontsize=14)
    # plt.tight_layout()
    # plt.savefig("priv/plots/trans2.png")
    # plt.show()
    
    # # Task 2.3
    
    # alpha_region_vals = np.linspace(0, 50e-3, 20)
    # G_arr = np.zeros((len(alpha_region_vals), 3))
    
    # E = 0.005
    # for P in [0.2, 0.4, 1.0]:
    #     for idx, alpha in enumerate(alpha_region_vals):
    #         p.alpha = nm2au(eV2au(alpha))
            
    #         nw = types.SimpleNamespace(\
    #                         dx=nm2au(4),
    #                         L=nm2au(p.L),
    #                         W=nm2au(p.W),
    #                         m=p.m_eff,
    #                         region_con = 2,
    #                         region = [0.2, 0.8]
    #                         )
            
    #         t_upup = transmission_spins(nw, E, [1, 0], [1, 1])
    #         t_updown = transmission_spins(nw, E, [1, 0], [0, 1])
    #         t_downup = transmission_spins(nw, E, [1, 0], [1, 0])
    #         t_downdown = transmission_spins(nw, E, [1, 0], [0, 0])

    #         G_arr[idx, 0] = ((1. + P) / 2.) * t_upup + ((1. - P) / 2.) * t_updown
    #         G_arr[idx, 1] = ((1. + P) / 2.) * t_downup + ((1. - P) / 2.) * t_downdown
    #         G_arr[idx, 2] = ((1. + P) / 2.) * G_arr[idx, 0] + ((1. - P) / 2.) * G_arr[idx, 1]
        
    #     colors = cm2c(cmap=cm_inferno, c_numb=13)
        
    #     line_plotter(alpha_region_vals, G_arr[:,0], xlabel=r"$\alpha$ [meV $\cdot$ nm]", ylabel="conductance", color=colors[3], linestyle="-", label=r'G$_{up}$')
    #     plt.plot(alpha_region_vals, G_arr[:,1], color=colors[7], linestyle='--', label=r'G$_{down}$')
    #     plt.plot(alpha_region_vals, G_arr[:,2], color=colors[11], linestyle='-', label=r'G')
    #     plt.legend(fontsize=14)
    #     plt.tight_layout()
        
    #     name_to_save = "cond2_P" + str(P) + ".png"
    #     save_path = os.path.join("priv/plots/", name_to_save)
        
    #     plt.savefig(save_path)
    #     plt.show()
        
    # Task 2.5
    
    E = 0.005
    p.alpha = eV2au(nm2au(18e-3))
    
    nw = types.SimpleNamespace(\
                        dx=nm2au(4),
                        L=nm2au(p.L),
                        W=nm2au(p.W),
                        m=p.m_eff,
                        region_con = 2,
                        region = [0.2, 0.8]
                        )
    
    den_up = np.matrix([[1,0],
                        [0,0]])
    den_down = np.matrix([[0,0],
                        [0,1]])
    
    sys=make_system(nw)
    
    wave_f=kwant.wave_function(sys, eV2au(E))(0)
    
    density_up_op = kwant.operator.Density(sys, den_up)
    density_down_op = kwant.operator.Density(sys,den_down)
    
    density_up_map = density_up_op(wave_f[0])
    density_down_map = density_down_op(wave_f[0])

    fig, ax = plt.subplots(2, 1, figsize=(10,3))
    kwant.plotter.map(sys, density_up_map, cmap=cm_inferno, ax=ax[0])
    kwant.plotter.map(sys, density_down_map, cmap=cm_inferno, ax=ax[1])
    ax[0].set_title("Spin up")
    ax[1].set_title("Spin down")
    plt.tight_layout()
    plt.savefig("priv/plots/spin2_1.png", dpi=150)
    plt.show()
    
    density_x = kwant.operator.Density(sys, p.sigma_x)
    density_y = kwant.operator.Density(sys, p.sigma_y)
    density_z = kwant.operator.Density(sys, p.sigma_z)
    
    density_x_map = density_x(wave_f[0])
    density_y_map = density_y(wave_f[0])
    density_z_map = density_z(wave_f[0])

    fig, ax = plt.subplots(3, 1, figsize=(10,5))
    kwant.plotter.map(sys, density_x_map, cmap=cm_inferno, ax=ax[0])
    kwant.plotter.map(sys, density_y_map, cmap=cm_inferno, ax=ax[1])
    kwant.plotter.map(sys, density_z_map, cmap=cm_inferno, ax=ax[2])
    ax[0].set_title(r"Spin s$_x$")
    ax[1].set_title(r"Spin s$_y$")
    ax[2].set_title(r"Spin s$_z$")
    plt.tight_layout()
    plt.savefig("priv/plots/spin2_2.png", dpi=150)
    plt.show()
        
if __name__ == "__main__":
    main()