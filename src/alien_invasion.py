import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
  """Manages game resources and behaviour"""

  def __init__(self):
    """Initializes the game and creates resources"""
    pygame.init()
    self.clock = pygame.time.Clock()
    self.settings = Settings()

    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    self.settings.screen_width = self.screen.get_rect().width
    self.settings.screen_height = self.screen.get_rect().height

    #self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()

  def run_game(self):
    """Initializes game main loop"""
    while True:
      self._check_events()
      self.ship.update()
      self._update_bullets()
      self._update_screen()
      self.clock.tick(60)

  def _check_events(self):
    """Manages key and mause events"""
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        self._check_keydown_events(event)
      elif event.type == pygame.KEYUP:
        self._check_keyup_events(event)

  def _check_keydown_events(self, event):
    """Responds to keydown events"""
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = True
    elif event.key == pygame.K_q:
      sys.exit()
    elif event.key == pygame.K_SPACE:
        self._fire_bullet()
  
  def _check_keyup_events(self, event):
    """Responds to keyup events"""
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = False
    if event.key == pygame.K_LEFT:
      self.ship.moving_left = False

  def _fire_bullet(self):
    """Creates a new bullet and adds it to the group"""
    if len(self.bullets) < self.settings.bullets_allowed:
      new_bullet = Bullet(self)
      self.bullets.add(new_bullet)

  def _update_bullets(self):
    """Updates the bullets position and deletes the old ones"""
    self.bullets.update()

    for bullet in self.bullets.copy():
      if bullet.rect.bottom <= 0:
        self.bullets.remove(bullet)

  def _update_screen(self):
    """Updates images and refreshes the screen"""
    self.screen.fill(self.settings.bg_color)
    
    for bullet in self.bullets.sprites():
       bullet.draw_bullet() 
    
    self.ship.blitme()

    pygame.display.flip()

if __name__ == '__main__':
  ai = AlienInvasion()
  ai.run_game()