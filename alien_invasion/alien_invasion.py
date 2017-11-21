import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

import game_functions as gf


def run_game():
    # Initialize game and create a game object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    play_button = Button(ai_settings, screen, "Play")

    # 创建存储游戏信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    scoreboard = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start game main loop
    while True:
        gf.check_events(ai_settings, stats, scoreboard, screen, ship, aliens,
                        bullets, play_button)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, stats, scoreboard, screen, ship,
                              bullets, aliens)
            gf.update_aliens(ai_settings, stats, scoreboard, screen, ship,
                             aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, scoreboard, ship, bullets,
                         aliens, play_button)


run_game()
