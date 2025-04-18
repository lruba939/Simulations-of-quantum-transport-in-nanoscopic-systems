## Singleton of parameters
# OrlowskiWojtek [git] inspired <3

class SimParams:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance._init_parameters()
        return cls._instance
    
    def _init_parameters(self):
        
        ## Converters
        self.hartree_to_meV = 27211.6
        self.bohr_radius = 0.0529    # [nm]

        ## System parameters
        self.omegax = 80. / self.hartree_to_meV
        self.omegay = 200. / self.hartree_to_meV
        self.reducted_mass = 0.24
        self.mstar = 0.24
        
        ## Simulation settings
        self.n = 9
        self.N = self.n**2
        self.dx = 1. / self.bohr_radius
        self.dx_denser = self.dx / 10.
        self.a = self.dx * (self.n-1) / 2.
        self.dim = self.N
        # self.dim = int((self.dx / self.dx_denser) * self.n)

        self.xk = []
        for k in range(self.N):
            self.xk.append(-1. * self.a + self.dx * int(k/self.n))
        
        self.yk = []
        for k in range(self.N):
            self.yk.append(-1. * self.a + self.dx * int(k%self.n))

        
    def alpha(self, xy, h=1):
        if xy == 'x':
            return h / (self.mstar * self.omegax)
        if xy == 'y':
            return h / (self.mstar * self.omegay)
        else: 
            print("\nIncorrect alpha() call!\nUse 'x' or 'y'.\n")
            return None
        
    def showParams(self):
        print("\n\n#################################\nSimulation and System Parameters:\n")
        for k, v in self.__dict__.items():
            if not k.startswith('_') and not isinstance(v, (list, dict, tuple)):
                print(f"{k} = {v}")
        print("\n#################################\n\n")