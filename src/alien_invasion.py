import sys

import pygame

from settings import Settings

class AlienInvasion:
  """Manages game resources and behaviour"""

  def __init__(self):
    """Initializes the game and creates resources"""
    pygame.init()
    self.clock = pygame.time.Clock()
    self.settings = Settings()

    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

  def run_game(self):
    """Initializes game main loop"""
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()

      self.screen.fill(self.settings.bg_color)

      pygame.display.flip()
      self.clock.tick(60)

if __name__ == '__main__':
  ai = AlienInvasion()
  ai.run_game()