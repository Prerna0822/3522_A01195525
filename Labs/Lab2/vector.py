
"""
Vector class to determine position.
Submitted By: Prerna Prerna, A01195525
              Saksham Bhardwaj, A01185352
"""


class Vector:

    def __init__(self, x, y, z):
        self.x_coordinate = x
        self.y_coordinate = y
        self.z_coordinate = y

    # Getter for returning x coordinate of the vector.
    def get_x(self):
        return self.x_coordinate

    # Getter for returning y coordinate of the vector.
    def get_y(self):
        return self.y_coordinate

    # Getter for returning z coordinate of the vector.
    def get_z(self):
        return self.z_coordinate

    ''' 
    Adding vector
    '''

    def add(self, vector):
        self.x_coordinate += vector.get_x()
        self.y_coordinate += vector.get_y()
        self.z_coordinate += vector.get_z()
    '''
    Returning vector as tuple.
    '''
    def tuple(self):
        return self.x_coordinate, self.y_coordinate, self.z_coordinate
    '''
    Formatting the tuple.
    '''
    def __str__(self):
        return f"{self.tuple()}"


'''Drive the program.'''


def main():
    vector1 = Vector(1, 2, 3)
    vector2 = Vector(3, 2, 1)
    print(f"Old Vector:{vector1}")
    vector1.add(vector2)
    print(f"New Vector:{vector1}")


if __name__ == "__main__":
    main()
