## Singleton of parameters
import numpy as np
from . import units

class SimParams:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance._init_parameters()
        return cls._instance
    
    def _init_parameters(self):

        ## System parameters
        self.E = 30e-3 # eV
        self.E = units.eV2au(self.E)
        
        self.V0 = 50e-3 #eV
        self.V0 = units.eV2au(self.V0)
        self.sigma = 10 #nm
        self.sigma = units.nm2au(self.sigma)
        
        self.B = 0.
        self.B = units.T2au(self.B)
        
        
        ## Simulation settings
        self.N = 100
        
    def set_E(self, newE):
        self.E = newE * 1e-3 # eV
        self.E = units.eV2au(self.E)

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