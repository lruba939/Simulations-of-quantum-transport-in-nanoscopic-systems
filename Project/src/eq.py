import kwant
import numpy as np
from . import units
from . import syst
from . import params

p = params.SimParams()

############################################################################################
##       Define various functions calculating the basic physical properties               ##
############################################################################################

#calculates the dispersion relation in the contact nr_lead in the range [-k_max,k_max] with nk points
def disperssion(nr_lead, k_max, nk):
    dx=p.dx
    sys=syst.make_system()
    momenta = np.linspace(-k_max*dx,k_max*dx,nk)
    bands=kwant.physics.Bands(sys.leads[nr_lead])
    energies=[bands(k) for k in momenta]
    return (momenta/dx)*units.nm2au(1.0), energies

#calculates the transmission coefficient
def transmission(E):
    E=units.eV2au(E)
    sys=syst.make_system()
    smatrix=kwant.smatrix(sys,E)
    t=smatrix.transmission(1,0)
    return t

#calculates the conductance - the Landauer formula is used
def conductance(Emax, ne):
    energies=np.linspace(0, Emax, ne)
    cond=[transmission(E) for E in energies]
    return energies, cond
    
def transmission_matrix(E):
    E = units.eV2au(E)
    sys = syst.make_system()
    smatrix = kwant.smatrix(sys, E)

    tup_down = smatrix.transmission((0, 0), (1, 1))
    tup_up = smatrix.transmission((0, 0), (1, 0))
    tdown_down = smatrix.transmission((0, 1), (1, 1))
    tdown_up = smatrix.transmission((0, 1), (1, 0))

    return tup_down, tup_up, tdown_down, tdown_up
    
def reflection_coeffs(E):
    E = units.eV2au(E)
    sys = syst.make_system()
    smatrix = kwant.smatrix(sys, E)

    Ree = smatrix.transmission((0, 0), (0, 0))
    Rhe = smatrix.transmission((0, 1), (0, 0))
    return Ree, Rhe