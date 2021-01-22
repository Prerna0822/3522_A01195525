import time
from datetime import datetime
from asteroid import Asteroid

'''
Create and maintains a list of asteroid objects in the field.
Submitted By: Prerna Prerna, A01195525
              Saksham Bhardwaj, A01185352
'''


class Controller:
    # One second in microseconds
    ONE_SECOND = 1000000

    ''' 
    Create Controller to track Asteroids.
    :param number as int (count of asteroids)
    '''

    def __init__(self, number):
        self._asteroids_list = []
        for i in range(number):
            random = Asteroid(Asteroid.random_radius(),
                              Asteroid.random_position(),
                              Asteroid.random_velocity(),
                              time.time())
            self._asteroids_list.append(random)

    ''' 
    Simulate Asteroid movement in one second increments.
    :param seconds as int 
    '''

    def simulate(self, seconds):
        current_time = datetime.now()
        difference_time = (Controller.ONE_SECOND - current_time.microsecond) / Controller.ONE_SECOND
        time.sleep(difference_time)

        for i in range(seconds):
            for asteroid in self._asteroids_list:
                print("Simulation Start Time" + str(datetime.now()))
                asteroid.move()
                print(asteroid)
                time.sleep(1)


'''Drive the program.'''


def main():
    controller = Controller(100)
    controller.simulate(2)


if __name__ == "__main__":
    main()
