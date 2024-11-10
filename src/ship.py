import pygame

class Ship:
  """The class that manages the ship"""

  def __init__(self, ai_game) -> None:
    """Initializes the ship and configures its initial position"""
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()

    self.image = pygame.image.load("images/ship.bmp")
    self.rect = self.image.get_rect()

    self.rect.midbottom = self.screen_rect.midbottom

  def blitme(self):
    """Prints the ship in the initial position"""
    self.screen.blit(self.image, self.rect)
