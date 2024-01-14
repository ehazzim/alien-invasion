import pygame

class Ship:
    """Class to manage ship"""

    def __init__(self, ai_game, width, height):
        """Initialize ship and set starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image and get rect
        original_image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(original_image, (width, height))
        self.rect = self.image.get_rect()

        # Start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store decimal value for ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update (self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x
        self.rect.x = self.x
    
    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)