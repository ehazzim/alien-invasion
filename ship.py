import pygame

class Ship:
    """Class to manage ship"""

    def __init__(self, ai_game, width, height):
        """Initialize ship and set starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image and get rect
        original_image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(original_image, (width, height))
        self.rect = self.image.get_rect()

        # Start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)