import kwant
import numpy as np
from . import units
from . import syst

############################################################################################
##       Define various functions calculating the basic physical properties               ##
############################################################################################

#calculates the dispersion relation in the contact nr_lead in the range [-k_max,k_max] with nk points
def disperssion(nw, nr_lead, k_max, nk):
    dx=nw.dx
    sys=syst.make_system(nw)
    momenta = np.linspace(-k_max*dx,k_max*dx,nk)
    bands=kwant.physics.Bands(sys.leads[nr_lead])
    energies=[bands(k) for k in momenta]
    return (momenta/dx)*units.nm2au(1.0), energies

#calculates the reflection and transmission coefficient
def transmission_reflection(nw, E):
    E=units.eV2au(E)
    sys=syst.make_system(nw)
    smatrix=kwant.smatrix(sys,E)
    r=smatrix.transmission(0,0)
    t=smatrix.transmission(1,0)
    return r, t

#calculates the transmission coefficient
def transmission(nw, E):
    E=units.eV2au(E)
    sys=syst.make_system(nw)
    smatrix=kwant.smatrix(sys,E)
    t=smatrix.transmission(1,0)
    return t

#calculates the conductance - the Landauer formula is used
def conductance(nw, Emax, ne):
    energies=np.linspace(0, Emax, ne)
    cond=[transmission(nw, E) for E in energies]
    return energies, cond

#plots the wave function of an electron with energy E incident in the contact nr_lead
def wave_function(nw, E, nr_lead):
    E=units.eV2au(E)
    sys=syst.make_system(nw)
    wave=kwant.wave_function(sys, E)
    density=(abs(wave(nr_lead))**2).sum(axis=0)
    kwant.plotter.map(sys,density)

#fplots the dos of an electron with energy E
def dos(nw, E):
    E=units.eV2au(E)
    sys=syst.make_system(nw)
    dos=kwant.ldos(sys, E)
    kwant.plotter.map(sys,dos)

#plots the current of an electron with energy E incident in the contact nr_lead in the state nr_mod
def current(nw, E, nr_lead, nr_mod):
    E=units.eV2au(E)
    sys=syst.make_system(nw)
    current = kwant.operator.Current(sys).bind()
    psi=kwant.wave_function(sys, E)(nr_lead)
    curr=current(psi[nr_mod])
    kwant.plotter.current(sys,curr)