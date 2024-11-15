import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

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

    self.stats = GameStats(self)

    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()
    self.aliens = pygame.sprite.Group()

    self._create_fleet()

    self.game_active = True

  def run_game(self):
    """Initializes game main loop"""
    while True:
      self._check_events()

      if self.game_active:
        self.ship.update()
        self._update_bullets()
        self._update_aliens()
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

    self._check_bullet_alien_collisions()

  def _check_bullet_alien_collisions(self): 
    collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    if not self.aliens:
      self.bullets.empty()
      self._create_fleet()

  def _create_fleet(self):
    """Create the fleet of aliens."""
    # Create an alien and keep adding aliens until there's no room left.
    # Spacing between aliens is one alien width and one alien height.
    alien = Alien(self)
    alien_width, alien_height = alien.rect.size

    current_x, current_y = alien_width, alien_height
    while current_y < (self.settings.screen_height - 10 * alien_height):
      while current_x < (self.settings.screen_width - 2 * alien_width):
        self._create_alien(current_x, current_y)
        current_x += 2 * alien_width

      # Finished a row; reset x value, and increment y value.
      current_x = alien_width
      current_y += 2 * alien_height
  
  def _create_alien(self, x_position, y_position):
    new_alien = Alien(self)
    new_alien.x = x_position
    new_alien.rect.x = x_position
    new_alien.rect.y = y_position
    self.aliens.add(new_alien)

  def _update_aliens(self):
    """Updates positions of aliens in the fleet"""
    self._check_fleet_edges()
    self.aliens.update()

    if pygame.sprite.spritecollideany(self.ship, self.aliens):
      self._ship_hit()
    
    self._check_aliens_bottom()

  def _check_fleet_edges(self):
    """Reacts to any alien reaching the border"""
    for alien in self.aliens.sprites():
      if alien.check_edges():
        self._change_fleet_direction()
        break

  def _change_fleet_direction(self):
    """Moves all the fleet down and changes direction"""
    for alien in self.aliens.sprites():
      alien.rect.y += self.settings.fleet_drop_speed
    self.settings.fleet_direction *= -1 

  def _update_screen(self):
    """Updates images and refreshes the screen"""
    self.screen.fill(self.settings.bg_color)
    
    for bullet in self.bullets.sprites():
       bullet.draw_bullet() 
    
    self.ship.blitme()
    self.aliens.draw(self.screen)

    pygame.display.flip()

  def _ship_hit(self):
    if self.stats.ships_left > 0:
      self.stats.ships_left -= 1
      self.aliens.empty()
      self.bullets.empty()

      self._create_fleet()
      self.ship.center_ship()

      sleep(0.5) 
    else:
      self.game_active = False

  def _check_aliens_bottom(self):
    for alien in self.aliens.sprites():
      if alien.rect.bottom >= self.settings.screen_height:
        self._ship_hit()
        break

if __name__ == '__main__':
  ai = AlienInvasion()
  ai.run_game()