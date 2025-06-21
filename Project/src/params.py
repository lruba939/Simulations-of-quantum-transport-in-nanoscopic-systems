## Singleton of parameters
import numpy as np
from . import units
import kwant

class SimParams:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance._init_parameters()
        return cls._instance
    
    def _init_parameters(self):
        ## Data
        self.Cu_dir = "data/Nb_Cu"
        self.Fe_dir = "data/Nb_Fe"
        self.output_path = ''
        
        ## System parameters
        self.Delta_x = 0.2 #nm
        self.dx = units.nm2au(self.Delta_x)
        self.a = 1.0 #nm
        self.L = int(1250) #nm
        self.sigma_law = np.array([[1,0],
                                   [0,2]])
        
        ## Simulation settings
        self.Delta = 0.25e-3 #eV
        self.Delta_val = units.eV2au(self.Delta)
        self.mu = 10e-3 #eV
        self.P = 0.0
        self.Z = 0.0
        self.t = 1 / (2 * self.dx**2)
        
    def h(self, x):
            if x < self.L * self.dx / 2:
                return self.P * units.eV2au(self.mu)
            else:
                return 0.0
    
    def delta_func(self, x):
            if x < self.L * self.dx / 2:
                return 0.0
            else:
                return self.Delta_val
            
    def potential_term(self, x):
            center = self.L * self.dx / 2
            return self.Z * units.eV2au(self.mu) * np.exp(-((x - center) ** 2) / (2 * units.nm2au(self.a)**2))

    def reset_to_defaults(self):
        self._init_parameters()
        
    def showParams(self):
        print("\n\n#################################\nSimulation and System Parameters:\n")
        for k, v in self.__dict__.items():
            if not k.startswith('_'):
                if not isinstance(v, (list, dict, tuple, np.ndarray)): #
                    print(f"{k} = {v}")
                else:
                    print(f"{k} = {v[:5]}")
        print("#################################\n\n")