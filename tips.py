# 提示类： 显示图片信息等
import pygame


class Tips:
    """提示类"""
    def __init__(self, sp_settings, screen, stats):
        """初始化得分板属性"""
        self.sp_settings = sp_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        # 提示信息字体和颜色
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 36)

        # 提示信息
        self.help_image = None
        self.help_rect = None
        self.prep_help()
        # 控制提示信息
        self.tips_image = None
        self.tips_image_rect = None
        self.prep_tips()

        # 准备剩余图片数量信息
        self.remains_image = None
        self.remains_rect = None
        self.prep_remains()

        # 已进行组计数
        self.select_count_image = None
        self.select_count_image_rect = None
        self.prep_select_count()

    def prep_tips(self):
        """"渲染操作提示信息为图片
        并将其放置于帮助信息下方"""
        self.tips_image = self.font.render(self.stats.tips_help_str, True,
                                           self.text_color, self.sp_settings.bg_color)
        # 将最高分置于屏幕顶部中央
        self.tips_image_rect = self.tips_image.get_rect()
        self.tips_image_rect.left = self.screen_rect.left + 20
        self.tips_image_rect.top = self.help_rect.bottom

    def prep_help(self):
        """渲染帮助信息为图片
        并放置于屏幕左上角"""
        self.help_image = self.font.render(self.stats.tips_tip_str, True,
                                           self.text_color, self.sp_settings.bg_color)
        # 将最高分置于屏幕顶部中央
        self.help_rect = self.help_image.get_rect()
        self.help_rect.left = self.screen_rect.left + 20
        self.help_rect.top = 20

    def prep_remains(self):
        """渲染剩余图片数量为图片
        并放置于屏幕右上角"""
        remains_str = str(self.stats.remains)
        self.remains_image = self.font.render(remains_str, True,
                                              self.text_color, self.sp_settings.bg_color)
        # 将最高分置于屏幕顶部中央
        self.remains_rect = self.remains_image.get_rect()
        self.remains_rect.right = self.screen_rect.right - 20
        self.remains_rect.top = 20

    def prep_select_count(self):
        """渲染选择计数为图片
        并放置于剩余图片下方"""
        select_count_str = str(len(self.stats.select_list))
        self.select_count_image = self.font.render(select_count_str, True,
                                                   self.text_color, self.sp_settings.bg_color)
        # 将最高分置于屏幕顶部中央
        self.select_count_image_rect = self.select_count_image.get_rect()
        self.select_count_image_rect.right = self.screen_rect.right - 20
        self.select_count_image_rect.top = self.remains_rect.bottom

    def show_tips(self):
        """显示提示信息"""
        self.screen.blit(self.help_image, self.help_rect)
        self.screen.blit(self.tips_image, self.tips_image_rect)
        self.screen.blit(self.remains_image, self.remains_rect)
        self.screen.blit(self.select_count_image, self.select_count_image_rect)
