# TODO THIS IS HOW TO MAKE A TODO
"""Program by William Stoneham"""
import sys, pygame
import time
import tkinter as tk
import threading
from queue import Queue
import random
import os
from Classes.Display import *
from Classes.Image import *
from Classes.Acceleration import *
from Classes.Road import *
from Classes.Car_Class import *
from Classes.Text import *
from Classes.Obstical import *
from Classes.collision import *

"""Init pygame and it's font associate"""
pygame.init()
pygame.font.init()

"""Version and other crap"""
GameName = "RockRacing"
Version = "1.5"
print(GameName + " by William Stoneham" + Version)

"""Defines the initial variables like the size of the screen, The clock and more"""
Game_width = 400
Game_height = 750
fps = 60
Top_Speed = 15
Acceleration = 0.001
Start_Acceleration = 0.02
Start_Acceleration_Stop = 5
x_change = 100
surface = Display(Game_width, Game_height, fps)
clock = pygame.time.Clock()
obstacle_chance = 100
len_between_ob_spawn = 10 * 60

"""Defines the pygame display"""
gameDisplay = pygame.display.set_mode((Game_width, Game_height), pygame.DOUBLEBUF | pygame.HWSURFACE, 32)
pygame.display.set_caption(GameName)

"""init custom text thingy"""
TEXT = pygame_text(gameDisplay)

"""defines the surfaces needed to create the game."""
carImg = Image(gameDisplay, "Car3.png", 82, 82, collision=True)
car_Left = Image(gameDisplay, "Car3_Left.png", 82, 82, collision=True)
car_Right = Image(gameDisplay, "Car3_Right.png", 82, 82, collision=True)
Road = Image(gameDisplay, "NewRoad.png", 400, 116, convert=True)
Road_Blank = Image(gameDisplay, "NewRoadblank.png", 400, 116, convert=True)
Back_Ground = Image(gameDisplay, "BlankRoad2.png", 400, 800, convert=True)
Tree_Stump = Image(gameDisplay, "TreeStump.png", 100, 100, collision=True)


# TODO FINISH SCORE SYSTEM
class score:
    def __init__(self):
        self.surface = pygame_text(gameDisplay)
        self.x = 5
        self.y = 200

    def update(self, score):
        self.surface.blit(score, 0, 5, size=24)


class MainMenu:
    def __init__(self):
        self.active = False


"""creates the road pieces"""
roads = []
for i in range(0, 8):
    if i % 2 == 0:
        i = RoadClass(i, True)
    else:
        i = RoadClass(i, False)
    roads.append(i)

"""Defines the Car"""
car = Car_Class(Game_height, x_change, car_Left, carImg, car_Right)


def GameLoop():
    """Defines the pygame display"""
    gameDisplay = pygame.display.set_mode((Game_width, Game_height), pygame.DOUBLEBUF | pygame.HWSURFACE, 32)
    pygame.display.set_caption(GameName)

    """defines the surfaces needed to create the game."""
    carImg = Image(gameDisplay, "Car3.png", 82, 82, collision=True)
    car_Left = Image(gameDisplay, "Car3_Left.png", 82, 82, collision=True)
    car_Right = Image(gameDisplay, "Car3_Right.png", 82, 82, collision=True)
    Road = Image(gameDisplay, "NewRoad.png", 400, 116, convert=True)
    Road_Blank = Image(gameDisplay, "NewRoadblank.png", 400, 116, convert=True)
    Back_Ground = Image(gameDisplay, "BlankRoad2.png", 400, 800, convert=True)
    Tree_Stump = Image(gameDisplay, "TreeStump.png", 100, 100, collision=True)

    # TODO  some sort of menu system. Maybe including an online mode.

    """creates the road pieces"""
    roads = []
    for i in range(0, 8):
        if i % 2 == 0:
            i = RoadClass(i, True)
        else:
            i = RoadClass(i, False)
        roads.append(i)

    """Defines the Car"""
    car = Car_Class(Game_height, x_change, car_Left, carImg, car_Right)

    """Invokes the Acceleration object"""
    Accelerate = Acceleration_Class(Acceleration, Start_Acceleration_Stop, Start_Acceleration, Top_Speed)

    """Creates obstacle list and resets the default maximum amount of obstacles"""
    obstacle = []
    Max_Obstacles = 0

    """sets Crashed to False"""
    crashed = False

    """Resets the game clock"""
    Frames = 0

    """Resets the score"""
    Score = 0

    while not crashed:
        """Main Game Loop"""
        speed = Accelerate.update()  # increases speed parameter
        Back_Ground.blit(0,
                         0)  # Displays the background. So if the road has imperfections the game would still look good

        """User Input system"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  ## What happens when the X button is pressed.
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    car.left()
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    car.right()

        for road_Class in list(roads):
            road_Class.move(speed, Game_height)
            ry = road_Class.posy
            if road_Class.type:
                Road.blit(0, ry)
            else:
                Road_Blank.blit(0, ry)

        """Obstacle system.
        Randomly generates an object to the display. Which will then be animated until it is completely of the screen 
        where it will be destroyed
        """
        if Frames % 25 == 0:
            if len(obstacle) < Max_Obstacles:
                obs = Obstacle_Class(Tree_Stump)
                obstacle.append(obs)
        for obstac in obstacle:
            if obstac.y >= Game_height:
                obstacle.remove(obstac)
            else:
                obstac.update(speed)
                if collision(car, obstac):
                    crashed = True
                    return Frames
        if Frames % len_between_ob_spawn == 0:
            Max_Obstacles += 1

        """updates car location and displays it to the screen"""
        car.update(speed)

        """Counts the amount of frames produced"""
        Frames += 1

        """Score"""
        Score = Frames / 60

        """Final update of display and tick of the clock"""
        pygame.display.update()
        clock.tick(60)


Frames = GameLoop()
pygame.quit()

print()
print("You're Score is: " + str(Frames))
print("press F2 to replay")
