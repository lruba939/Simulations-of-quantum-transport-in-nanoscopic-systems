## Singleton of parameters
import numpy as np

class SimParams:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance._init_parameters()
        return cls._instance
    
    def _init_parameters(self):
        
        ## Converters
        self.hartree_to_eV = 27.2116
        self.bohr_radius = 0.0529    # [nm]
        self.m0 = 1. # atomic units
        self.kB = 3.167e-6 # Boltzmann const.

        ## System parameters
        self.E = 0.01 / self.hartree_to_eV # eV
        self.d_Al = 5. / self.bohr_radius # nm
        self.d_Ga = 5. / self.bohr_radius # nm
        self.m_Al = (0.063+0.083*0.3)*self.m0
        self.m_Ga = 0.063*self.m0
        self.U_Al = 0.27 / self.hartree_to_eV # eV
        self.U_Ga = 0.0 / self.hartree_to_eV # eV
        self.L = 15 / self.bohr_radius # nm
        self.mu_s = 87e-3 / self.hartree_to_eV # eV
        self.mu_d = 87e-3 / self.hartree_to_eV # eV
        self.T = 77. # K
        
        ## Simulation settings
        self.N = 100
        self.z = np.linspace(0, self.L, self.N)
        self.m = np.array([0 for _ in range(self.N)], dtype=float)
        self.U = np.array([0 for _ in range(self.N)], dtype=float)
        self.k = np.array([0 for _ in range(self.N)], dtype=complex)
        
    def set_sys(self, case, bias=0):     # case: 1-one layer, 2-two layers
        match case:
            case 1:
                for i in range(self.N):
                    if self.z[i] < 5.0 / self.bohr_radius:
                        self.U[i] = self.U_Ga - bias*(self.z[i]/self.z[-1])
                        self.m[i] = self.m_Ga
                    elif self.z[i] >= 5.0 / self.bohr_radius and self.z[i] < 10.0 / self.bohr_radius:
                        self.U[i] = self.U_Al - bias*(self.z[i]/self.z[-1])
                        self.m[i] = self.m_Al
                    elif self.z[i] >= 10.0 / self.bohr_radius:
                        self.U[i] = self.U_Ga - bias*(self.z[i]/self.z[-1])
                        self.m[i] = self.m_Ga
            case 2:
                for i in range(self.N):
                    if self.z[i] < 1.0 / self.bohr_radius:
                        self.U[i] = self.U_Ga - bias*(self.z[i]/self.z[-1])
                        self.m[i] = self.m_Ga
                    elif self.z[i] >= 1.0 / self.bohr_radius and self.z[i] < 6.0 / self.bohr_radius:
                        self.U[i] = self.U_Al - bias*(self.z[i]/self.z[-1])
                        self.m[i] = self.m_Al
                    elif self.z[i] >= 6.0 / self.bohr_radius and self.z[i] < 9.0 / self.bohr_radius:
                        self.U[i] = self.U_Ga - bias*(self.z[i]/self.z[-1])
                        self.m[i] = self.m_Ga
                    elif self.z[i] >= 9.0 / self.bohr_radius and self.z[i] < 14.0 / self.bohr_radius:
                        self.U[i] = self.U_Al - bias*(self.z[i]/self.z[-1])
                        self.m[i] = self.m_Al
                    elif self.z[i] >= 14.0 / self.bohr_radius:
                        self.U[i] = self.U_Ga - bias*(self.z[i]/self.z[-1])
                        self.m[i] = self.m_Ga
            case _:
                print("Wrong parameter in the set_sys function!")
            
        self.set_k()
                
    def set_k(self):
        for i in range(self.N):
            self.k[i] = np.sqrt(2*self.m[i]*(self.E - self.U[i] + 0j))
        
    def set_E(self, newE):
        self.E = newE / self.hartree_to_eV
        self.set_k()

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