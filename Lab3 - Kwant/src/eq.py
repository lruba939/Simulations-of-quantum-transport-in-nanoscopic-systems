import kwant
import numpy as np
from . import units
from . import syst

############################################################################################
##       Define various functions calculating the basic physical properties               ##
############################################################################################

#calculates the dispersion relation in the contact nr_lead in the range [-k_max,k_max] with nk points
def disperssion(nw, nr_lead, k_max, nk, is_ring=0):
    dx=nw.dx
    sys=syst.make_system(nw, is_ring)
    momenta = np.linspace(-k_max*dx,k_max*dx,nk)
    bands=kwant.physics.Bands(sys.leads[nr_lead])
    energies=[bands(k) for k in momenta]
    return (momenta/dx)*units.nm2au(1.0), energies

#calculates the reflection and transmission coefficient
def transmission_reflection(nw, E, is_ring=0):
    E=units.eV2au(E)
    sys=syst.make_system(nw, is_ring)
    smatrix=kwant.smatrix(sys,E)
    r=smatrix.transmission(0,0)
    t=smatrix.transmission(1,0)
    return r, t

#calculates the transmission coefficient
def transmission(nw, E, lead_in=1, lead_out=0, is_ring=0):
    E=units.eV2au(E)
    sys=syst.make_system(nw, is_ring)
    smatrix=kwant.smatrix(sys,E)
    t=smatrix.transmission(lead_in, lead_out)
    return t

#calculates the conductance - the Landauer formula is used
def conductance(nw, Emax, ne, lead_in=1, lead_out=0, is_ring=0):
    energies=np.linspace(0, Emax, ne)
    cond=[transmission(nw, E, lead_in, lead_out, is_ring) for E in energies]
    return energies, cond

#plots the wave function of an electron with energy E incident in the contact nr_lead
def wave_function(nw, E, nr_lead, ax = None, is_ring=0):
    E=units.eV2au(E)
    sys=syst.make_system(nw, is_ring)
    wave=kwant.wave_function(sys, E)
    density=(abs(wave(nr_lead))**2).sum(axis=0)
    kwant.plotter.map(sys,density, ax = ax)

#fplots the dos of an electron with energy E
def dos(nw, E, is_ring=0):
    E=units.eV2au(E)
    sys=syst.make_system(nw, is_ring)
    dos=kwant.ldos(sys, E)
    kwant.plotter.map(sys,dos)

#plots the current of an electron with energy E incident in the contact nr_lead in the state nr_mod
def current(nw, E, nr_lead, nr_mod, ax = None, is_ring=0):
    E=units.eV2au(E)
    sys=syst.make_system(nw, is_ring)
    current = kwant.operator.Current(sys).bind()
    psi=kwant.wave_function(sys, E)(nr_lead)
    curr=current(psi[nr_mod])
    kwant.plotter.current(sys,curr, ax = ax)