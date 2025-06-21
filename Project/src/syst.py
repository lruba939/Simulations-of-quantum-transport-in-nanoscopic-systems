import kwant
import numpy as np
from . import params
from . import units

############################################################################################
## Defining the system, we need to define the functions describing the hopping energies   ##
## to the same node and the neighbor nodes. We do it in the functions onsite(),           ##
## hopping_x(), and hopping_y().
############################################################################################

p = params.SimParams()

#definition of the system for simulations
def make_system():
    
    def onsite(site):
        (xi,) = site.pos
        t = p.t
        mu = units.eV2au(p.mu)
        h = p.h(xi)
        delta = p.delta_func(xi)
        V = p.potential_term(xi)

        return np.array(
            [[2 * t - mu - h + V, delta], [delta, -(2 * t - mu + h + V)]]
        )

    def onsite_normal(site):
        (xi,) = site.pos
        t = p.t
        mu = units.eV2au(p.mu)
        h = p.h(xi)
        return np.array([[2 * t - mu - h, 0], [0, -(2 * t - mu + h)]])

    def hopping_x(sitei, sitej):
        t = 1 / (2 * p.dx**2)
        return np.matrix(
            [[-t, 0], [0, t]],
        )

    sys = kwant.Builder()
    lat = kwant.lattice.chain(p.dx, norbs=2)
    sys[(lat(i) for i in range(p.L))] = onsite
    sys[lat.neighbors()] = hopping_x
    
    lead_left = kwant.Builder(
        kwant.TranslationalSymmetry((-p.dx,)), conservation_law=p.sigma_law
    )
    lead_left[lat(0)] = onsite_normal
    lead_left[lat.neighbors()] = hopping_x
    sys.attach_lead(lead_left)

    def onsite_sc(site):
        (xi,) = site.pos
        t = p.t
        mu = units.eV2au(p.mu)
        delta = p.Delta_val

        return np.array([[2 * t - mu, delta], [delta, -(2 * t - mu)]])

    def hopping_sc(sitei, sitej):
        t = 1 / (2 * p.dx**2)
        return np.matrix([[-t, 0], [0, t]])

    lead_right = kwant.Builder(kwant.TranslationalSymmetry((p.dx,)))
    lead_right[lat(0)] = onsite_sc
    lead_right[lat.neighbors()] = hopping_sc
    sys.attach_lead(lead_right)

    sys = sys.finalized()
    return sys