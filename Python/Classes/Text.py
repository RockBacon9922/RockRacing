import pygame


class pygame_text:
    """
    An easy to use text display tool for pygame.
    :arg game_display
    :return nothing
    """
    def __init__(self, game_display):
        self.game_display = game_display

    """
    Used to display text
    :arg string of text, font as a string, color as RGB and coordinates
    :returns displays text to screen
    """
    def blit(self, text, x, y, size=12, font="calibri", color=(255, 255, 255)):
        my_font = pygame.font.SysFont(font, size)
        text_surface = my_font.render(str(text), False, color)
        self.game_display.blit(text_surface, (x, y))
