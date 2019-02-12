import sys
import pygame
from bullet import Bullet
from Aliens.Alien import Alien


def check_keydown_event(event, ship, setting, screen, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(bullets, setting, screen, ship)
    elif event.key == pygame.K_q:   # 退出快捷键
        sys.exit()


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship, setting, screen, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship, setting, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


# 更新屏幕
def update_screen(my_game_setting, screen, ship, bullets, aliens):
    screen.fill(my_game_setting.bg_color)
    ship.drawimage()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()


def update_bullet(aliens, bullets):
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)


# 开火子弹设置
def fire_bullets(bullets, setting, screen, ship):
    if len(bullets) < setting.bullet_maxcount:
        new_bullet = Bullet(setting, screen, ship)
        bullets.add(new_bullet)


# 计算每可以创建多少个
def get_number_alien_x(game_setting, alien_width):
    available_space_x = game_setting.screen_width - 2 * alien_width
    num_alien_x = int(available_space_x / (2 * alien_width))
    return num_alien_x  # 每行可以创建多少个飞船


# 计算可以创建多少行
def get_number_alien_y(game_setting, ship_hieght, alien_height):
    '''计算每行可以创建多少行'''
    available_space_y = game_setting.screen_height - 3 * ship_hieght - alien_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(game_setting, screen, aliens, alien_num, row_number):
    alien = Alien(screen, game_setting)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_num
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(game_setting, screen, aliens, ship):
    alien = Alien(game_setting, screen)
    '''创建一群外星人'''
    num_alien_x = get_number_alien_x(game_setting, alien.rect.width)
    num_alien_y = get_number_alien_y(game_setting, ship.rect.height, alien.rect.height)

    for aline_index_line_y in range(num_alien_y):
        for aline_index_line_x in range(num_alien_x):
            create_alien(game_setting, screen, aliens, aline_index_line_x,aline_index_line_y)


def check_fleet_edges(game_setting, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_setting,aliens)
            break


def change_fleet_direction(game_setting, aliens):
    for alien in aliens.sprites():
        alien.rect.y += game_setting.fleet_drop_speed
    game_setting.fleet_direction *= -1


def update_alien(game_setting, aliens):
    check_fleet_edges(game_setting, aliens)
    aliens.update()

