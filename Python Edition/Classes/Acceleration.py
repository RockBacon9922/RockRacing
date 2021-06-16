import sys
import math
class Acceleration_Class:
    """Works out the speed of the car and other objects"""
    def __init__(self, acceleration, start_acceleration_max, start_acceleration, top_speed):
        self.speed = 1
        self.acceleration = acceleration
        self.start_acceleration_max = start_acceleration_max
        self.topspeed = top_speed
        self.start_acceleration = start_acceleration
    def update(self):
        """
        This increases speed based off a mathematical curve to create smooth gameplay.
        :arg self
        :return: an increased speed value. Intended to be put in the game loop.
        """

        if self.topspeed >= self.speed >= self.start_acceleration_max:
            self.speed += self.acceleration
        if self.speed <= self.start_acceleration_max:
            self.speed += self.start_acceleration
        return self.speed