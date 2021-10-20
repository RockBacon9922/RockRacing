import random


class Obstacle_Class:
    """Creates obstacles for game"""
    """x_locations are [10, 110, 210, 310]"""
    def __init__(self, obstacle):
        self.x_locations = [10, 110, 210, 310]
        self.obstacle = obstacle
        self.y = -self.obstacle.height
        pick = random.randint(0, 3)
        self.map = self.obstacle.map
        self.x = self.x_locations[pick]
        self.collision = False
        self.xlocs = self.obstacle.xlocs
        self.ylocs = self.obstacle.ylocs

    def update(self, speed):
        self.y += speed
        self.obstacle.blit(self.x, self.y)


