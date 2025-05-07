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
def make_system(nw):
    m=nw.m
    dx=nw.dx
    L=nw.L
    W=nw.W
    
    x0 = units.nm2au(L)
    y0 = 0

    def onsite(site):
        (x, y) = site.pos
        t=1.0/(2.0*m*dx*dx)
        
        # scattering potential
        x_part = ( (x - x0) / p.sigma )**2
        y_part = ( (y - y0) / p.sigma )**2
        # V = p.V0*np.exp( -(x_part+y_part) )
        V = 0
        
        return 4*t + V

    def hopping_x(sitei, sitej):
        (xi, yi) = sitei.pos
        (xj, yj) = sitej.pos
        t=1.0/(2.0*m*dx*dx)
        t = t*np.exp(-1j / 2. * p.B * (xj - xi) * (yj + yi) )
        
        return -t
    
    def hopping_y(sitei, sitej):
        (xi, yi) = sitei.pos
        (xj, yj) = sitej.pos
        t=1.0/(2.0*m*dx*dx)
        t = t*np.exp(-1j / 2. * p.B * (xj - xi) * (yj + yi) )
         
        return -t

    # We subsequently define:
    # 1. Define the system - function kwant.Builder()  
    # 2. Describe the geometry of the grid - kwant.lattice.square(dx, norbs=1)
    # 3. Fill the Hamiltonian matrix
    sys = kwant.Builder()  
    lat = kwant.lattice.square(dx, norbs=1)
    sys[(lat(i,j) for i in range(L) for j in range(-W,W))]=onsite
    sys[(kwant.builder.HoppingKind((-1,0), lat, lat))] = hopping_x
    sys[(kwant.builder.HoppingKind((0,-1), lat, lat))] = hopping_y
    
    
    #attach the left contact to the system
    lead_left = kwant.Builder(kwant.TranslationalSymmetry((-dx, 0)))    
    lead_left[(lat(0,j) for j in range(-W,W))]=onsite
    lead_left[(kwant.builder.HoppingKind((-1,0), lat, lat))] = hopping_x
    lead_left[(kwant.builder.HoppingKind((0,-1), lat, lat))] = hopping_y
    sys.attach_lead(lead_left)
    
    
    #attach the right contact to the system
    lead_right = kwant.Builder(kwant.TranslationalSymmetry((dx, 0)))    
    lead_right[(lat(0,j) for j in range(-W,W))]=onsite
    lead_right[(kwant.builder.HoppingKind((-1,0), lat, lat))] = hopping_x
    lead_right[(kwant.builder.HoppingKind((0,-1), lat, lat))] = hopping_y
    sys.attach_lead(lead_right)
    
    #finalize the system
    sys = sys.finalized()
    return sys