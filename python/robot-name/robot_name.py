from collections import defaultdict
from string import ascii_uppercase
from random import randint

robot_names = defaultdict(lambda: 0)

class Robot:
    def __init__(self):
        Robot.reset(self)

    def reset(self):
        name = Robot.get_unique_name()
        while robot_names[name] != 0:
            name = Robot.get_unique_name()
        robot_names[name] = 1
        self.name = name
    
    def get_unique_name(self):
        return ascii_uppercase[randint(0,25)] + ascii_uppercase[randint(0,25)] + str(randint(1,9)) + str(randint(1,9)) + str(randint(1,9))

