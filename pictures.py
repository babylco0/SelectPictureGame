# 选择的图片类
import pygame
import os
from pygame.sprite import Sprite
from random import randint


class Pictures(Sprite):
    """供用户选择的图片类"""

    def __init__(self, sp_settings, screen, file_path):
        """初始化图片类属性
        sp_settings: 配置
        screen: 屏幕
        file_path: 图片文件名
        quadrant: 所属象限
        """
        super().__init__()
        self.sp_settings = sp_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.file_path = file_path
        pic_info = file_path.split('.')
        pic_info = pic_info[0].split('_')
        self.pic_shape = pic_info[0]
        self.pic_size = pic_info[1]
        self.pic_color = pic_info[2]
        self.quadrant = 0  # 象限信息
        self.progresses = []  # 选择历程
        self.image = None
        self.image_rect = None

    def info(self):
        """返回图片信息"""
        return [self.pic_shape, self.pic_size, self.pic_color, str(self.quadrant)]

    def update(self, center=None):
        """重新加载图片"""
        self.image = pygame.image.load(os.path.join('images/', self.file_path))
        self.image_rect = self.image.get_rect()
        if center:
            self.image_rect.center = center
        else:
            # 随机生成一个坐标
            x = randint(0, self.sp_settings.screen_width)
            y = randint(0, self.sp_settings.screen_height)
            self.image_rect.x = x
            self.image_rect.y = y

    def blitme(self):
        """加载所有图片"""
        self.screen.blit(self.image, self.image_rect)
