import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, setting, screen, ship):
        super().__init__()

        self.screen = screen

        self.image = pygame.image.load('resources/bullet2.bmp')
        self.rect = self.image.get_rect()
        # 设置子弹起始正确位置
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 设置表示子弹位置的值
        self.y = float(self.rect.y)
        self.speed_factor = setting.bullet_speed_factor

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
        