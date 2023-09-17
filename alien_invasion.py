import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Main class will manage game assets and behavior"""

    def __init__(self):
        """Initialize game and create game resources"""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Calculate reference_size as a percentage of the screen width or height
        screen_width = self.settings.screen_width
        screen_height = self.settings.screen_height
        reference_percentage = 0.1
        reference_size = min(screen_width, screen_height) * reference_percentage

        self.ship = Ship(self, reference_size)

        # Set background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start main game loop"""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw screen during each pass through loop
            self.screen.fill(self.bg_color)
            self.ship.blitme()

            # Make most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make game instance and run game
    ai = AlienInvasion()
    ai.run_game()