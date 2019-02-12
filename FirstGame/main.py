import pygame
from Settings.GameSettings import GameSettings
from ShipClass.Ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏窗口
    pygame.init()
    my_game_setting = GameSettings()
    screen = pygame.display.set_mode((my_game_setting.screen_width,my_game_setting.screen_height))
    my_ship = Ship(my_game_setting, screen)
    pygame.display.set_caption("MyGame")
    # 设置背景颜色
    bg_color = my_game_setting.bg_color
    # 创建子弹集合
    bullets = Group()
    aliens = Group()
    gf.create_fleet(my_game_setting, screen, aliens, my_ship)

    # game loop
    while True:
        gf.check_events(my_ship, my_game_setting, screen, bullets)
        my_ship.update()
        gf.update_bullet(aliens, bullets)
        gf.update_alien(my_game_setting, aliens)
        gf.update_screen(my_game_setting, screen, my_ship, bullets, aliens)


run_game()
