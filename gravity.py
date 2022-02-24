import numpy as np

from quick_maths import vector_magnitude

G = 6.67e-11

class Gravity:

    def __init__(self, obj1, obj2):
        """Initializes the gravity engine between two objects.
        INPUTS:
            obj1, obj2 - The two objects that are orbiting each other.
        """

        self.obj1 = obj1
        self.obj2 = obj2

    def force_gravity():
        """Calculates the force of gravity between two objects.
        INPUTS:
            obj1, obj2 - The two objects that are interacting.
        OUTPUTS:

        """

        #The Newtonian model for gravity is given to us as F = Gm1m2/r21^2
        #To set this as a 3D vector, Fvec = Gm1m2/||r21||^3 * rvec
        
        r21 = obj2.position - obj1.position
        r21_mag = vector_magnitude(r21_vec)
        F21 = G*obj1.mass*obj2.mass/(r21_mag**3) * r21_vec
        F12 = -F21

        return F21, F12

    def movement(self, massive_object, net_force, start_time, end_time):
        '''
        Takes the massive object and the net force acting on it to calculate the changes in acceleration, velocity, and 
        position using Runge Kutta

        #example 8.5 in Computational Physics by Mark Newman does something similar
        '''
        position = massive_object.position
        velocity = massive_object.velocity
        acceleration = massive_object.acceleration
        
        dt = (end_time - start_time) / 100000
        times = np.arange(start_time, end_time, dt)



