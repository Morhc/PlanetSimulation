import numpy as np

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



        pass
