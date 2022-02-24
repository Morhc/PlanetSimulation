import numpy as np

from quick_maths import vector_magnitude

class Gravity:

    def __init__(self, obj1, obj2):
        """Initializes the gravity engine between two objects.
        INPUTS:
            obj1, obj2 - The two objects that are orbiting each other.
        """

        self.obj1 = obj1
        self.obj2 = obj2

    def force_gravity(self):
        """Calculates the force of gravity between two objects.
        INPUTS:
            obj1, obj2 - The two objects that are interacting.

        OUTPUTS:
            Outputs the Newtonian gravitational force between the objects.
        """

        G = 6.67e-11

        #The Newtonian model for gravity is given to us as F = Gm1m2/r21^2.
        #To set this as a 3D vector, Fvec = Gm1m2/||r21||^3 * rvec.

        r21_vec = self.obj2.position - self.obj1.position
        r21_mag = vector_magnitude(r21_vec)

        F21 = G*self.obj1.mass*self.obj2.mass/(r21_mag**3) * r21_vec
        F12 = -F21

        return F21, F12
