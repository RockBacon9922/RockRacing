"""Program by William Stoneham 2020"""
import tkinter as tk
import os

root = tk.Tk()


class Display(object):
    """Defines Display parameters"""

    def __init__(self, pygame_width, pygame_height, fps):
        self.width = pygame_width
        self.height = pygame_height
        self.dimensions = self.width, self.height
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.fps = fps
        print("size of display")
        print(str(self.screen_width) + " : " + str(self.screen_height))
        self.displayloc_x = (self.screen_width / 2) - (self.width / 2)
        self.displayloc_y = 60
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (self.displayloc_x, self.displayloc_y)
