import math
from random import randint
from datetime import datetime
from vector import Vector
"""
Creating Asteroid class
   Submitted By: Prerna Prerna, A01195525
                 Saksham Bhardwaj, A01185352
"""

class Asteroid:
    # Assigning unique id to asteroid.
    asteroid_id = 1
    # Minimum Radius of asteroid.
    ASTEROID_MIN_RADIUS = 1
    # Maximum Radius of asteroid.
    ASTEROID_MAX_RADIUS = 4
    # Minimum Position of asteroid.
    ASTEROID_MIN_POS = 0
    # Maximum Position of asteroid.
    ASTEROID_MAX_POS = 100
    # Minimum Velocity of asteroid.
    ASTEROID_MIN_VELOCITY = -5
    # Maximum velocity of asteroid.
    ASTEROID_MAX_VELOCITY = 5

    def __init__(self, radius, position, velocity, timestamp):
        self.asteroid_circumference = 2 * math.pi * radius
        self.asteroid_position = position
        self.asteroid_velocity = velocity
        self.asteroid_timestamp = timestamp
        self.asteroid_id = Asteroid.increment_Asteroid_id()

    # Return Asteroid ID after incrementing it
    @classmethod
    def increment_Asteroid_id(cls):
        cls.asteroid_id += 1
        return cls.asteroid_id

    """
        Return random radius by using minimum and maximum radius of asteroid. 
    """
    @classmethod
    def random_radius(cls):
        return randint(cls.ASTEROID_MIN_RADIUS, cls.ASTEROID_MAX_RADIUS)

    """ Return random position of the vector within the range of maximum and minimum position."""
    @classmethod
    def random_position(cls):
        return Vector(randint(cls.ASTEROID_MIN_POS, cls.ASTEROID_MAX_POS),
                      randint(cls.ASTEROID_MIN_POS, cls.ASTEROID_MAX_POS),
                      randint(cls.ASTEROID_MIN_POS, cls.ASTEROID_MAX_POS))

    """ 
    Return random velocity of the vector within the range of maximum and minimum velocity
    """
    @classmethod
    def random_velocity(cls):
        return Vector(randint(cls.ASTEROID_MIN_VELOCITY, cls.ASTEROID_MAX_VELOCITY),
                      randint(cls.ASTEROID_MIN_VELOCITY, cls.ASTEROID_MAX_VELOCITY),
                      randint(cls.ASTEROID_MIN_VELOCITY, cls.ASTEROID_MAX_VELOCITY))

    # Getter method for returning position of the vector.

    def get_position(self):
        return self.asteroid_position

    """"
    Setter method for position of the vector.
    :param position: Vector
    """

    def set_position(self, position):
        self.asteroid_position = position

    # Getter method for returning the velocity of the vector.

    def get_velocity(self):
        return self.asteroid_velocity

    """
     Setter method for velocity of the vector.
    :param velocity: Vector
     """

    def set_velocity(self, velocity):
        self.asteroid_velocity = velocity

    """
    Setter method for minimum radius of the asteroid.
    :param rad: int
    """

    def set_minimum_radius(self, rad):
        self.ASTEROID_MIN_RADIUS = rad

    """
        Setter method for maximum radius of the asteroid.
        :param rad: int
    """

    def set_maximum_radius(self, rad):
        self.ASTEROID_MAX_RADIUS = rad

    '''
      Setter method for minimum position of the asteroid.
      :param pos: int
    '''

    def set_minimum_position(self, pos):
        self.ASTEROID_MIN_POS = pos

    '''
        Setter method for maximum position of the asteroid.
        :param pos: int
    '''

    def set_maximum_pos(self, pos):
        self.ASTEROID_MAX_POS = pos

    '''
        Setter for minimum velocity of the asteroid.
        :param vel: int 
    '''

    def set_minimum_velocity(self, vel):
        self.ASTEROID_MIN_VELOCITY = vel

    '''
    Setter for the maximum velocity of the asteroid.
    :param vel: int
    '''

    def set_maximum_velocity(self, vel):
        self.ASTEROID_MAX_VELOCITY = vel

    '''
    Method to move the asteroid using the current velocity.
    Return position as Vector
    '''

    def move(self):
        self.asteroid_position.add(self.asteroid_velocity)
        return self.asteroid_position

    '''Format Asteroid with unique ID, circumference, position, velocity, and time created.'''

    def __str__(self):
        return f"Asteroid: {self.asteroid_id} Moved!" \
               f"\nPosition of the asteroid: {self.asteroid_position} " \
               f"\nVelocity of the asteroid: {self.asteroid_velocity} " \
               f"\nCircumference of the asteroid: {self.asteroid_circumference} " \
               f"\nTimestamp of the asteroid: {self.asteroid_timestamp}"


'''Drive the program.'''


def main():
    pos = Vector(50, 55, 60)
    v1 = Vector(1, 2, 1)
    v2 = Vector(3, 2, 1)
    asteroid = Asteroid(4, pos, v1, datetime.now())
    v1.add(v2)
    asteroid.set_velocity(v1)
    print(asteroid)
    print(asteroid.move())


if __name__ == "__main__":
    main()
