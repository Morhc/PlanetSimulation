class Massive_Object:
    def __init__(self, mass, radius, position, velocity, acceleration, colour):
        '''
        initializes the massive objects to add objects to the gravity simulation

        Requires: position, velocity, acceleration are numpy arrays with the x,y,z components
        '''
        
        self.mass = mass
        self.radius = radius
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.colour = colour

    def update_position(self, new_position):
        self.position = new_position

    def update_velocity(self, new_velocity):
        self.velocity = new_velocity

    def update_acceleration(self, new_acceleration):
        self.acceleration = new_acceleration
