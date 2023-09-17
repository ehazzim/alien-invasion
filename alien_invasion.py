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

        # Specify the width and height for the ship
        ship_width = 120
        ship_height = 200

        self.ship = Ship(self, ship_width, ship_height)

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