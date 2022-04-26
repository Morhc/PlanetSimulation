import numpy as np
import scipy.interpolate as int
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

    def solver(time, condition) :

        position = condition.position
        velocity = condition.velocity
        acceleration = condition.acceleration

        dt = (end_time - start_time) / 100000

        solns = np.array([pos_ode(time, position, velocity),
                          vel_ode(time, velocity, acceleration),
                          acc_ode(time, acceleration, position)])

        return solns


def EulerCromer(timestep):

    G, Ms, AU, secToYear = 6.674E-11, 1.989E30, 1.496E11, 60*60*24*365

    semi_major = 76**(2/3)
    rmax = 2*semi_major - 0.509 #works this way sorry wish i knew why i cant start at rmin
    vx, vy = 0, sqrt(G*Ms*(2/(rmax*AU) - 1/(semi_major*AU)))*secToYear/AU #in AU/year
    x, y = rmax, 0 #in AU

    ret_x, ret_y = [x], [y]

    fac = G*Ms*secToYear*secToYear/AU/AU/AU #this gives non-circular answer vs 4pi^2

    time = 0
    vx_i, vy_i, x_i, y_i= '', '', '', ''

    max_dist, max_speed = -1, -1

    while time <= 76 + timestep:

        if time == 0: vx_i, vy_i, x_i, y_i= vx, vy, x, y

        r_i = sqrt(x_i**2+y_i**2)

        a_i = fac/r_i**2

        vx_i_next = vx_i - a_i*timestep*(x_i/r_i)
        x_i_next = x_i + vx_i_next*timestep

        vy_i_next = vy_i - a_i*timestep*(y_i/r_i)
        y_i_next = y_i + vy_i_next*timestep

        time+=timestep

        ret_x.append(x_i)
        ret_y.append(y_i)
        x_i, y_i, vx_i, vy_i = x_i_next, y_i_next, vx_i_next, vy_i_next

        if abs(x_i) > max_dist: max_dist = abs(x_i) #the way this is defined, the x-axis is naturally longer
        if abs(vy_i) > max_speed: max_speed = abs(vy_i)
        elif abs(vx_i) > max_speed: max_speed = abs(vx_i)

    return ret_x, ret_y, max_dist, max_speed        


    def movement(self, massive_object, net_force, start_time, end_time):
        '''
        Takes the massive object and the net force acting on it to calculate the changes in acceleration, velocity, and
        position using Runge Kutta

        #example 8.5 in Computational Physics by Mark Newman does something similar
        '''

        #dt = (end_time - start_time) / 100000
        times = np.linspace(start_time, end_time, 100000)

        solutions = int.solve_ivp(solver, (start_time, end_time), massive_object, 'RK45', t_eval=times,
                                  dense_output = True)
