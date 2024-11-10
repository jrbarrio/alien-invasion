from typing import Any
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
  """Manages bullets shooted from the ship"""

  def __init__(self, ai_game) -> None:
    super().__init__()
    self.screen = ai_game.screen
    self.settings = ai_game.settings
    self.color = self.settings.bullet_color

    # Creates a rectangle for the bullet and moves it to the right place
    self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
    self.rect.midtop = ai_game.ship.rect.midtop

    # Stores bullet position as a float
    self.y = float(self.rect.y)

  def update(self):
    """Moves the bullet up in the screen"""
    self.y -= self.settings.bullet_speed
    self.rect.y = self.y

  def draw_bullet(self):
    pygame.draw.rect(self.screen, self.color, self.rect)