import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''初始化外星人飞船'''
    def __init__(self, screen, setting):
        super(Alien, self).__init__()
        self.screen = screen
        self.game_setting = setting

        # 加载外星人飞船图像，并设置rect属性
        self.image = pygame.image.load('resources/alien1.bmp')
        self.rect = self.image.get_rect()

        # 放置飞船
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    # 绘制飞船
    def draw_alien(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.game_setting.fleet_direction ==1:
            self.x += self.game_setting.alien_speed_factor
            self.rect.x = self.x
        elif self.game_setting.fleet_direction == -1:
            self.x -= self.game_setting.alien_speed_factor
            self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
