class Settings:
  """A class to store all Alien Invasion configurations"""

  def __init__(self) -> None:
    """Initializes game configuration"""

    # Screen configuration
    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = (230, 230, 230)

    self.ship_speed = 1.5
    self.ship_limit = 3

    # Bullets configuration
    self.bullet_speed = 5.0
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = (60, 60, 60)
    self.bullets_allowed = 30

    self.alien_speed = 5.0
    self.fleet_drop_speed = 20
    self.fleet_direction = -1
