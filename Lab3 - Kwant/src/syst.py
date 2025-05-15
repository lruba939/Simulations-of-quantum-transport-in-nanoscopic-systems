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
def make_system(nw, is_ring = 0):
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
        V = p.V0*np.exp( -(x_part+y_part) )
        # V = 0
        
        return 4*t + V

    def hopping_x(sitei, sitej):
        (xi, yi) = sitei.pos
        (xj, yj) = sitej.pos
        t=1.0/(2.0*m*dx*dx)
        t = t*np.exp(-1j / 2. * p.B * (xi - xj) * (yi + yj) )
        
        return -t
    
    def hopping_y(sitei, sitej):
        (xi, yi) = sitei.pos
        (xj, yj) = sitej.pos
        t=1.0/(2.0*m*dx*dx)
        t = t*np.exp(-1j / 2. * p.B * (xi - xj) * (yi + yj) )
         
        return -t

    # We subsequently define:
    # 1. Define the system - function kwant.Builder()  
    # 2. Describe the geometry of the grid - kwant.lattice.square(dx, norbs=1)
    # 3. Fill the Hamiltonian matrix
    if is_ring == 0:
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
        
    elif is_ring == 1:
        R1 = nw.R1
        R2 = nw.R2
        
        def ring(pos):
            (x, y) = pos
            r2 = x**2 + y**2

            if((x <= -R2 + 50) and (x > -R2 - L * dx / 2)):
                return - W * dx < y < W * dx

            if((x >= 0) and (x < L * dx / 2)):
                top_site = -W * dx < y + (R1 + R2)/2 < W * dx 
                bot_site = -W * dx < y - (R1 + R2)/2 < W * dx

                return (top_site or bot_site)

            return ((R1 ** 2 < r2 < R2 ** 2 and x < 0) )
        
        lat = kwant.lattice.square(dx, norbs=1)
        sys = kwant.Builder()

        sys[lat.shape(ring, (-50, R1 + 50))] = onsite

        sys[(kwant.builder.HoppingKind((-1,0), lat, lat))] = hopping_x
        sys[(kwant.builder.HoppingKind((0,-1), lat, lat))] = hopping_y

        #attach the left contact to the system
        lead_left = kwant.Builder(kwant.TranslationalSymmetry((-dx, 0)))    
        lead_left[(lat(0,j) for j in range(-W,W))]=onsite
        lead_left[(kwant.builder.HoppingKind((-1,0), lat, lat))] = hopping_x
        lead_left[(kwant.builder.HoppingKind((0,-1), lat, lat))] = hopping_y
        sys.attach_lead(lead_left)
        
        top_idx = np.round(((R1 + R2) / 2) / dx)

        # attach the right top contact to the system
        lead_top_right = kwant.Builder(kwant.TranslationalSymmetry((dx, 0)))    
        lead_top_right[(lat(0,j + top_idx) for j in range(-W,W))]=onsite
        lead_top_right[(kwant.builder.HoppingKind((-1,0), lat, lat))] = hopping_x
        lead_top_right[(kwant.builder.HoppingKind((0,-1), lat, lat))] = hopping_y
        sys.attach_lead(lead_top_right)

        # attach the right bot contant to the system
        lead_bot_right = kwant.Builder(kwant.TranslationalSymmetry((dx, 0)))    
        lead_bot_right[(lat(0,j - top_idx + 1) for j in range(-W,W))]=onsite
        lead_bot_right[(kwant.builder.HoppingKind((-1,0), lat, lat))] = hopping_x
        lead_bot_right[(kwant.builder.HoppingKind((0,-1), lat, lat))] = hopping_y
        sys.attach_lead(lead_bot_right)
        
        #finalize the system
        sys = sys.finalized()
        
    else: print("Wrong geometry!")
    
    return sys