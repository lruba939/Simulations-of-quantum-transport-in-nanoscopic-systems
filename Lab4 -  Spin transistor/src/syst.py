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

    def onsite(site):
        t=1.0/(2.0*m*dx*dx)
        
        const_val = 1/2. * 1/2. * p.g
        bracket_part = p.B_x*p.sigma_x + p.B_y*p.sigma_y + p.B_z*p.sigma_z
        
        if(nw.region_con == 1):
            # print("True")
            if(site.pos[0] >= nw.region[0]*p.L*dx and site.pos[0] <= nw.region[1]*p.L*dx):
                if(nw.mag_reg_dir == 'X'):
                    sigma = p.sigma_x
                if(nw.mag_reg_dir == 'Y'):
                    sigma = p.sigma_y
                if(nw.mag_reg_dir == 'Z'):
                    sigma = p.sigma_z
                bracket_part = bracket_part + nw.mag_region_val*sigma
        
        result = 4*t*p.I + const_val*bracket_part
        
        return result

    def hopping_x(site_i, site_j):
        t=1.0/(2.0*m*dx*dx)
        t_SO = 1/2. * p.alpha / dx
        
        if(nw.region_con == 2):
            if(site_i.pos[0] >= nw.region[0]*p.L*dx and site_i.pos[0] <= nw.region[1]*p.L*dx):
                part1 = 1j * t_SO * p.sigma_y
            else:
                part1 = 0
        else:
            part1 = 1j * t_SO * p.sigma_y
            
        result = -t*p.I + part1
        
        return result

    def hopping_y(site_i, site_j):
        t=1.0/(2.0*m*dx*dx)
        t_SO = 1/2. * p.alpha / dx
        
        if(nw.region_con == 2):
            if(site_i.pos[0] >= nw.region[0]*p.L*dx and site_i.pos[0] <= nw.region[1]*p.L*dx):
                part1 = -1j * t_SO * p.sigma_x
            else:
                part1 = 0
        else:
            part1 = -1j * t_SO * p.sigma_x
        
        result = t*p.I + part1
        
        return result

    # We subsequently define:
    # 1. Define the system - function kwant.Builder()  
    # 2. Describe the geometry of the grid - kwant.lattice.square(dx, norbs=1)
    # 3. Fill the Hamiltonian matrix
    sys = kwant.Builder()  
    lat = kwant.lattice.square(dx, norbs=2)
    sys[(lat(i,j) for i in range(p.L) for j in range(0,p.W))] = onsite
    sys[(kwant.builder.HoppingKind((-1,0), lat, lat))] = hopping_x
    sys[(kwant.builder.HoppingKind((0,-1), lat, lat))] = hopping_y
    
    
    #attach the left contact to the system
    lead_left = kwant.Builder(kwant.TranslationalSymmetry((-dx, 0)),conservation_law=p.sigma_law)
    lead_left[(lat(0,j) for j in range(0,p.W))]=onsite
    lead_left[(kwant.builder.HoppingKind((-1,0), lat, lat))] = hopping_x
    lead_left[(kwant.builder.HoppingKind((0,-1), lat, lat))] = hopping_y
    sys.attach_lead(lead_left)
    
    
    #attach the right contact to the system
    lead_right = kwant.Builder(kwant.TranslationalSymmetry((dx, 0)),conservation_law=p.sigma_law)
    lead_right[(lat(0,j) for j in range(0,p.W))]=onsite
    lead_right[(kwant.builder.HoppingKind((-1,0), lat, lat))] = hopping_x
    lead_right[(kwant.builder.HoppingKind((0,-1), lat, lat))] = hopping_y
    sys.attach_lead(lead_right)
    
    #finalize the system
    sys = sys.finalized()
    return sys