import pygame


class Ship:

    def __init__(self, my_setings, screen):
        self.screen = screen

        # 加载图像
        self.image = pygame.image.load('resources/ship1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.settings = my_setings

        # 将ship放置在屏幕下方
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

        self.center = float(self.rect.centerx)

    def drawimage(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor

        self.rect.centerx = self.center
