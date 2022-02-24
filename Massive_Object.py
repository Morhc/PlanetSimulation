class Massive_Object:
    def __init__(self, mass, radius, position, velocity, acceleration):
        '''
        initializes the massive objects to add objects to the gravity simulation

        Requires: position, velocity, acceleration are numpy arrays with the x,y,z components
        '''
        self.mass = mass
        self.radius = radius
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        