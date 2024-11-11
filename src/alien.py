import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
  """An alien in the fleet"""

  def __init__(self, ai_game):
    super().__init__()
    self.screen = ai_game.screen
    self.settings = ai_game.settings
    
    self.image = pygame.image.load("images/alien.bmp")
    self.rect = self.image.get_rect()

    self.rect.x = self.rect.width
    self.rect.y = self.rect.height
    
    self.x = float(self.rect.x)

  def check_edges(self):
    """Returns True if the alien is on the screen border"""
    screen_rect = self.screen.get_rect()
    return (self.rect.right >= screen_rect.right) or (self.rect.left == 0)

  def update(self):
    "Moves alien to the right"
    self.x += self.settings.alien_speed * self.settings.fleet_direction
    self.rect.x = self.x