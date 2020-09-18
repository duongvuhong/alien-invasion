"""Settings class"""

class Settings():
    """A class to store all settings for Alien Invasion."""

    # Screen settings.
    screen_width = 600
    screen_height = 400
    bg_color = (230, 230, 230)

    # Game settings.
    # how quickly the game speeds up
    speedup_scale = 1.1
    # fleet_direction of 1 represents right, -1 represents left.
    fleet_direction = 1

    # Ship settings.
    ship_limit = 3
    ship_speed_factor = 0.5
    ship_image = 'images/ship.png'

    # Bullet settings.
    bullet_width = 3
    bullet_height = 10
    bullet_color = (60, 60, 60)
    bullet_speed_factor = 0.5
    bullets_allowed = 3

    # Alien settings.
    fleet_drop_speed = 10
    alien_speed_factor = 0.1
    alien_image = 'images/alien.png'

    # Scoring.
    alien_points = 50
    score_scale = 1.5

    @staticmethod
    def reset():
        """Reset settings that change throughout the game."""
        Settings.ship_speed_factor = 0.5
        Settings.bullet_speed_factor = 0.5
        Settings.alien_speed_factor = 0.1

        # Scoring.
        Settings.alien_points = 50

        # Fleet direction
        Settings.fleet_direction = 1

    @staticmethod
    def increase_speed():
        """Increase speed settings and alien point values."""
        Settings.ship_speed_factor *= Settings.speedup_scale
        Settings.bullet_speed_factor *= Settings.speedup_scale
        Settings.alien_speed_factor *= Settings.speedup_scale

        Settings.alien_points = int(Settings.alien_points * Settings.score_scale)
