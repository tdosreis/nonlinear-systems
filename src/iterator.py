import numpy as np
from scipy.integrate import ode

class Attractor(): 
    def __init__(self, attractor=None, seed=101, tf=100, dt=0.01): 
        self.time = np.arange(start=0, stop=tf, step=dt)
        self.Y = np.empty((3, self.time.size))
        self.attractor = attractor

    def iterate(self):
        
        r = self.__set_initial_value()
        
        self.Y[:, 0] = np.random.random(size=3)
        
        for i, t in enumerate(self.time):
            r.integrate(t)
            self.Y[:, i] = r.y
        
        return self.Y    
    
    def __set_integrator(self): 
        r = ode(self.attractor).set_integrator('dopri5')
        return r
    
    def __set_initial_value(self): 
        r = self.__set_integrator()
        r.set_initial_value(self.Y[:, 0], t=0)
        return r