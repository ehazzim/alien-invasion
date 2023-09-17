import pygame

class Ship:
    """Class to manage ship"""

    def __init__(self, ai_game, reference_size):
        """Initialize ship and set starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image and get rect
        original_image = pygame.image.load('images/ship.png')
        self.reference_size = reference_size

        # Calculate the aspect ratio
        aspect_ratio = original_image.get_width() / original_image.get_height()

        # Scale the image while maintaining aspect ratio
        new_width = int(reference_size * aspect_ratio)
        new_height = int(reference_size / aspect_ratio)  # Calculate height to maintain aspect ratio
        self.image = pygame.transform.scale(original_image, (new_width, new_height))
        self.rect = self.image.get_rect()

        # Start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)