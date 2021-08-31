"""RockBacon 2021, RockRacing Online"""
import os
import sys
import tkinter as tk
import pygame
from communication import rocksocket
from Classes.Text import *

root = tk.Tk()

"""initialize pygame and its other modules"""
pygame.init()
pygame.font.init()

"""Constants"""
GAMENAME = "RockRacing - ONLINE"
VERSION = "1.0"
FPS = 69
TOP_SPEED = 22
CLOCK = pygame.time.Clock()

print(GAMENAME + " by William Stoneham" + VERSION)

