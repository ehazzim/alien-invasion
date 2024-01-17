import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in fleet."""

    def __init__(self,ai_game):
        """Initalize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect

        # Start each new alien near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's exact horizontal position
        self.x = float(self.rect.x)