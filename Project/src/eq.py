import kwant
import numpy as np
from . import units
from . import syst
from . import params

p = params.SimParams()

############################################################################################
##       Define various functions calculating the basic physical properties               ##
############################################################################################

#calculates the transmission coefficient
def transmission(E):
    E=units.eV2au(E)
    sys=syst.make_system()
    smatrix=kwant.smatrix(sys,E)
    t=smatrix.transmission(1,0)
    return t
    
def reflection_coeffs(E):
    E = units.eV2au(E)
    sys = syst.make_system()
    smatrix = kwant.smatrix(sys, E)

    Ree = smatrix.transmission((0, 0), (0, 0))
    Rhe = smatrix.transmission((0, 1), (0, 0))
    return Ree, Rhe

def conductance(energies):
    G = []
    for E in energies:
        Ree, Rhe = reflection_coeffs(E)
        G_val = 1 - Ree + Rhe
        G.append(G_val)
    return G