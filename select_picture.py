# 选择图片游戏
import os
import pygame
import sys

from pygame.sprite import Group

from settings import Settings
from pictures import Pictures
import game_functions as gf
from pictures_stats import PicturesStats
from tips import Tips
from statistic import Statistic
import easygui


def run_game():
    """运行图片选择游戏"""
    # 初始化屏幕对象
    pygame.init()
    sp_settings = Settings()
    screen = pygame.display.set_mode((sp_settings.screen_width,
                                      sp_settings.screen_height))
    pygame.display.set_caption('Select Picture')
    # gf.generate_pictures(sp_settings)  # 生成图片库（首次使用时需要）
    files = os.listdir('images')  # 获取images下所有图片名称
    # 加载所有图片
    all_pictures = Group()
    selected_pictures = Group()
    unselected_pictures = Group()
    optional_pictures = Group()
    for file in files:
        pics = Pictures(sp_settings, screen, file)
        pics.update()
        all_pictures.add(pics)
    # 初始化剩余图片数量
    stats = PicturesStats(len(all_pictures.sprites()))
    gf.choice_pictures(stats, all_pictures, selected_pictures, unselected_pictures, optional_pictures)
    # 提示信息
    tips = Tips(sp_settings, screen, stats)
    # 统计图表
    st_chart = Statistic(sp_settings, screen)
    # 弹出登录框
    user_name = easygui.enterbox('Pls input you name...', title='')
    while not user_name:  # 输入正确的名字或按cancel结束循环
        if user_name is None:  # cancel 退出程序
            sys.exit()
        user_name = easygui.enterbox('Pls input you name...', title='')

    easygui.msgbox('Welcome %s' % (user_name,))
    st_chart.load_history(user_name + '.txt')
    pygame.display.set_caption(user_name.title() + 'Select Picture ...')
    # 无限循环
    while True:
        # 监听事件
        gf.check_events(sp_settings, screen, stats, st_chart, all_pictures, user_name,
                        selected_pictures, unselected_pictures, optional_pictures)
        gf.update_help_string(sp_settings, stats, optional_pictures)
        gf.update_tips(tips)
        gf.update_screen(sp_settings, screen, stats, tips, st_chart, all_pictures,
                         selected_pictures, unselected_pictures, optional_pictures)


run_game()
