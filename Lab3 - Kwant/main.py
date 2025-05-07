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
    nw = types.SimpleNamespace(\
                        dx=nm2au(2),
                        L=int(100),
                        W=int(20),
                        m=0.014 
                        )

    sys=make_system(nw)
    kwant.plot(sys, site_color=lambda site: sys.hamiltonian(site,site), fig_size=(10,5), colorbar=False, show=False, num_lead_cells=2);
    plt.show()

    momenta, energies = disperssion(nw, 0, .1, 200)
    plt.figure(figsize=(4,4))
    plt.plot(momenta, np.asarray(energies)/eV2au(1.0),'k-')
    plt.tick_params(axis='both', which='major', labelsize=22)
    plt.ylim((0,.2))  
    plt.xlim((-0.5,.5))  
    plt.xlabel("k [1/nm]",fontsize=22)
    plt.ylabel("E [eV]",fontsize=22)
    plt.show()

    energies, cond=conductance(nw, 0.2, 100)
    plt.figure(figsize=(8,4))
    plt.plot(energies, cond,'k-')
    plt.tick_params(axis='both', which='major', labelsize=22)
    plt.xlabel("E [eV]",fontsize=22)
    plt.ylabel("G [2e^2/h]",fontsize=22)
    plt.show()
    
    # wave_function(nw, 0.1, 0)
        
    # # dos(nw, 0.1)
    
    # current(nw, 0.1, 0, 0)

if __name__ == "__main__":
    main()