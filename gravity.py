import numpy as np
import scipy.interpolate as int
from Massive_Object import Massive_Object
from quick_maths import vector_magnitude

G = 6.67e-11

class Gravity:

    def __init__(self, obj1, obj2, end_time):
        """Initializes the gravity engine between two objects.
        INPUTS:
            obj1, obj2 - The two objects that are orbiting each other.
        """

        self.obj1 = obj1
        self.obj2 = obj2
        end_time = end_time*365*24*60*60 #convert to seconds
        self.times = np.linspace(0,end_time, 10000) 

    def force_gravity(self, position, obj):
        """Calculates the force of gravity between two objects.
        INPUTS:
            obj1, obj2 - The two objects that are interacting.
        OUTPUTS:

        """

        #The Newtonian model for gravity is given to us as F = Gm1m2/r21^2
        #To set this as a 3D vector, Fvec = Gm1m2/||r21||^3 * rvec

        r21 = self.obj2.position - position
        r21_mag = vector_magnitude(r21)
        F21 = G*obj.mass*self.obj2.mass/(r21_mag**3) * r21
        F12 = -F21

        return F21
    
    def f(self, gen, obj):

        pos, vel = gen
        f_vel = self.force_gravity(pos, obj)/obj.mass
        f_pos = vel
        return np.vstack((f_pos,f_vel))

    def RK4(self):
        dt = (self.times[-1]-self.times[0])/self.times.size
        for t in self.times:
            pos = self.obj1.position[-1]
            vel = self.obj1.velocity[-1]
            gen = np.array([pos, vel])
            k1 = dt*self.f(gen,self.obj1)
            k2 = dt*self.f(gen+k1/2, self.obj1)
            k3 = dt*self.f(gen+k2/2, self.obj1)
            k4 = dt*self.f(gen+k3, self.obj1)
            gen = gen + (1/6)*(k1+2*k2+2*k3+k4)  
            new_pos, new_vel = gen[0,:], gen[1,:]
            self.obj1.update_position(new_pos)
            self.obj1.update_velocity(new_vel)