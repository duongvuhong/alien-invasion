import os

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (3200, 100)

def run_game():
    """ main game function """
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(screen, "Play")

    # Create an instance to store game statistics, and a scoreboard.
    stats = GameStats(ai_settings)
    score_board = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, score_board, play_button, ship,
            aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, score_board, ship, aliens,
                bullets)
            gf.update_aliens(ai_settings, screen, stats, score_board, ship, aliens,
                bullets)

        gf.update_screen(ai_settings, screen, stats, score_board, ship, aliens,
            bullets, play_button)

if __name__ == "__main__":
    run_game()
