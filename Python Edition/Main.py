# TODO THIS IS HOW TO MAKE A TODO
"""Program by William Stoneham"""
import sys, pygame
import time
import tkinter as tk
import threading
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

"""Defines the pygame display"""
gameDisplay = pygame.display.set_mode((Game_width, Game_height), pygame.DOUBLEBUF | pygame.HWSURFACE, 32)
pygame.display.set_caption(GameName)

"""init custom text thingy"""
TEXT = pygame_text(gameDisplay)

"""defines the surfaces needed to create the game."""
Road = Image(gameDisplay, "NewRoad.png", 400, 116, convert=True)
Road_Blank = Image(gameDisplay, "NewRoadblank.png", 400, 116, convert=True)
Back_Ground = Image(gameDisplay, "BlankRoad2.png", 400, 800, convert=True)

"""creates the road pieces"""

"""Defines the Car"""
car = Car_Class(Game_height, x_change, car_Left, carImg, car_Right)


def GameLoop():
    # TODO  some sort of menu system. Maybe including an online mode.

    """creates the road pieces"""

    """Defines the Car"""
    car = Car_Class(Game_height, x_change, car_Left, carImg, car_Right)

    """Invokes the Acceleration object"""

    """Creates obstacle list and resets the default maximum amount of obstacles"""
    obstacle = []
    Max_Obstacles = 0

    """sets Crashed to False"""
    crashed = False

    """Resets the game clock"""
    Frames = 0

    """Resets the score"""
    Score = 0

    """Acceleration invoke"""
    Acceleration = 1

    """Creates some initial roads"""
    roads = []
    Road.height

    while not crashed: 
        """road"""
        for road in roads:
            pass

    """Final update of display and tick of the clock"""
    pygame.display.update()
    clock.tick(60)


Frames = GameLoop()
pygame.quit()