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

        # Scale the alien image
        new_width = 50
        aspect_ratio = self.image.get_width() / self.image.get_height()
        new_height = int(new_width / aspect_ratio)
        
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        self.rect = self.image.get_rect()

        # Start each new alien near top left of screen
        self.rect.x = 0
        self.rect.y = 0

        # Store alien's exact horizontal position
        self.x = float(self.rect.x)