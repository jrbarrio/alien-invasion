import pygame

class Ship:
  """The class that manages the ship"""

  def __init__(self, ai_game) -> None:
    """Initializes the ship and configures its initial position"""
    self.screen = ai_game.screen
    self.settings = ai_game.settings
    self.screen_rect = ai_game.screen.get_rect()

    self.image = pygame.image.load("images/ship.bmp")
    self.rect = self.image.get_rect()

    self.rect.midbottom = self.screen_rect.midbottom

    self.x = float(self.rect.x)

    self.moving_right = False
    self.moving_left = False

  def update(self):
    """Updates ship position"""
    if self.moving_right:
      self.x += self.settings.ship_speed
    elif self.moving_left:
      self.x -= self.settings.ship_speed

    self.rect.x = self.x

  def blitme(self):
    """Prints the ship in the initial position"""
    self.screen.blit(self.image, self.rect)
