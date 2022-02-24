import numpy as np

from Massive_Object import Massive_Object
from gravity import Gravity

def main():

    Msun = 1.99e30
    Rsun = 696e6
    AU = 1.496e11

    #sun and earth, starting at rest
    m1, m2 = Msun, Msun/1.3e6
    r1, r2 = Rsun, 0.009*Rsun
    p1, p2 = np.array([0, 0, 0]), np.array([AU/np.sqrt(3), AU/np.sqrt(3), AU/np.sqrt(3)])
    v1, v2 = np.array([0, 0, 0]), np.array([0, 0, 0])
    a1, a2 = np.array([0, 0, 0]), np.array([0.006, 0.006, 0])

    obj1 = Massive_Object(m1, r1, p1, v1, a1) #the Sun
    obj2 = Massive_Object(m2, r2, p2, v2, a2) #the Earth

    F21, F12 = Gravity(obj1, obj2).force_gravity()

    print(F12, F21)

if __name__ == '__main__':
    main()
