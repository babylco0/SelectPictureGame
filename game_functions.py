# 选择图片游戏功能函数集合
import pygame
import turtle
import time
import sys
from turtle_draw import TurtleDraw
from random import choice


def generate_pictures(sp_settings):
    """生成所有可选图形"""
    for s in sp_settings.pic_sizes:
        for c in sp_settings.pic_colors:
            for t in sp_settings.pic_shapes:
                tri = TurtleDraw("images/%s_%d_%s" % (t, s, c), s, c, t)
                tri.generate()
    turtle.bye()  # 关闭乌龟画图


def choice_pictures(stats, all_pictures, selected_pictures, unselected_pictures, optional_pictures):
    """选择图片显示到屏幕
    从all中选择X张图片，存放至optional中
    并将这X张图片，移至selected中
    如果all中不足X张图片，则从unselected中选择不足的图片
    如果all为空，则将selected移至all
    重复选择，直到all中仅有一张图片结束"""
    optional_pictures.empty()  # 清除上一次选择
    if len(all_pictures.sprites()) <= 4:  # 先从已选择图片中选择
        for pic in selected_pictures.sprites():
            all_pictures.add(pic)
        selected_pictures.empty()
    if len(all_pictures.sprites()) == 1:  # 仅剩余一张图片
        optional_pictures.add(all_pictures.sprites()[0])
        all_pictures.empty()
    else:
        for _ in range(4):  # 选择4张图片
            if all_pictures:  # 从所有图片中选择
                pic = choice(all_pictures.sprites())
                optional_pictures.add(pic)
                all_pictures.remove(pic)
            else:  # 从未选图片中选择
                pic = choice(unselected_pictures.sprites())
                optional_pictures.add(pic)
                unselected_pictures.remove(pic)
    # 更新图片信息
    stats.remains = len(all_pictures.sprites()) + len(selected_pictures.sprites()) + len(optional_pictures)


def check_events(sp_settings, screen, stats, st_chart, all_pictures, user_name,
                 selected_pictures, unselected_pictures, optional_pictures):
    """响应鼠标和按键事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 退出
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_selected_picture(sp_settings, stats, st_chart, all_pictures,
                                   selected_pictures, unselected_pictures,
                                   optional_pictures, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # 自动选择
                stats.ai_selecting = not stats.ai_selecting
            elif event.key == pygame.K_LSHIFT:  # 显示统计信息
                stats.show_statistic = not stats.show_statistic
            elif event.key == pygame.K_KP_ENTER:  # 保存至文件
                save_selections(stats, st_chart, user_name)
            elif event.key == pygame.K_ESCAPE:  # 退出
                sys.exit()
            elif event.key == pygame.K_0:  # shift + 0 清空历史记录
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    clear_history(st_chart, user_name)


def show_progresses(sp_settings, stats, st_chart,
                    all_pictures, selected_pictures, unselected_pictures, optional_pictures):
    """显示图片选择历程"""
    stats.is_saved = False
    if len(stats.select_list) < sp_settings.select_list_number:
        for pic in optional_pictures.sprites():
            # 生成图表
            create_bars(sp_settings, st_chart, stats)
            stats.select_list.append(pic.info())
        reselect(stats, all_pictures, selected_pictures, unselected_pictures, optional_pictures)
    else:
        stats.ai_selecting = False


def create_bars(sp_settings, st_chart, stats):
    """生成柱状图"""
    for pic in stats.select_list:
        st_chart.shapes[pic[0]] += 1
        st_chart.sizes[pic[1]] += 1
        st_chart.colors[pic[2]] += 1
        st_chart.quadrants[pic[3]] += 1


def reselect(stats, all_pictures, selected_pictures, unselected_pictures, optional_pictures):
    """重新选择图片"""
    for pic in optional_pictures.sprites():
        unselected_pictures.add(pic)
    for pic in unselected_pictures.sprites():
        all_pictures.add(pic)
        unselected_pictures.remove(pic)
    #  重新选择图片
    choice_pictures(stats, all_pictures, selected_pictures, unselected_pictures, optional_pictures)


def check_selected_picture(sp_settings, stats, st_chart, all_pictures,
                           selected_pictures, unselected_pictures,
                           optional_pictures, mouse_x, mouse_y):
    """响应鼠标点击图片事件"""
    # 仅剩余一张图片时 显示选择历程
    if len(optional_pictures.sprites()) == 1:
        pic = optional_pictures.sprites()[0]
        if pic.image_rect.collidepoint(mouse_x, mouse_y):
            show_progresses(sp_settings, stats, st_chart, all_pictures,
                            selected_pictures, unselected_pictures,
                            optional_pictures)
    # 将选中的图片放入selected 将未选中的图片放入unselected
    else:
        selected_picture = None
        for pic in optional_pictures.sprites():
            if pic.image_rect.collidepoint(mouse_x, mouse_y):
                selected_pictures.add(pic)
                optional_pictures.remove(pic)
                selected_picture = pic
        if selected_picture:
            add_progresses(selected_picture, optional_pictures.sprites())
            for pic in optional_pictures.sprites():
                unselected_pictures.add(pic)
            #  重新选择图片
            choice_pictures(stats, all_pictures, selected_pictures, unselected_pictures, optional_pictures)


def add_progresses(selected, unselected):
    """图片添加选择历程"""
    unselected_list = []
    for pic in unselected:
        unselected_list.append([pic.quadrant, pic])
    selected.progresses.append(unselected_list)


def random_choice(sp_settings, stats):
    """机器随机选择图片"""
    if stats.remains > 1:
        positions = []
        for x in range(2):
            for y in range(2):
                positions.append([sp_settings.screen_width / 4 + sp_settings.screen_width / 2 * x,
                                  sp_settings.screen_height / 4 + sp_settings.screen_height / 2 * y])
        return choice(positions)
    else:
        return sp_settings.screen_width / 2, sp_settings.screen_height / 2


def update_help_string(sp_settings, stats, optional_pictures):
    """更新提示信息"""
    # 修改帮助提示信息
    if len(stats.select_list) >= sp_settings.select_list_number:
        if not stats.is_saved:
            stats.tips_tip_str = 'LSHIFT to show statistic...ENTER to save...ESC to exit...'
        else:
            stats.tips_tip_str = 'ESC to exit...'
        stats.tips_help_str = 'All Done...'
    elif len(optional_pictures) == 1:
        stats.tips_help_str = 'Click picture to continue...'
    else:
        stats.tips_help_str = 'Click picture to select...'


def update_screen(sp_settings, screen, stats, tips, st_chart, all_pictures,
                  selected_pictures, unselected_pictures, optional_pictures):
    """更新屏幕"""
    screen.fill(sp_settings.bg_color)

    # 更新可选择图片
    if len(stats.select_list) >= sp_settings.select_list_number or stats.show_statistic:
        # 显示统计信息
        update_charts(st_chart)
        st_chart.show_statistics()
    elif len(optional_pictures.sprites()) == 1:  # 仅剩余一张图片
        # 将图片置于屏幕中央
        pic = optional_pictures.sprites()[0]
        pic.update((sp_settings.screen_width / 2,
                    sp_settings.screen_height / 2))
        pic.blitme()
    elif len(optional_pictures.sprites()) >= 4:
        for x in range(2):
            for y in range(2):
                pic = optional_pictures.sprites()[x * 2 + y]
                pic.quadrant = (x * 2 + y + 1)
                pic.update((sp_settings.screen_width / 4 + sp_settings.screen_width / 2 * x,
                            sp_settings.screen_height / 4 + sp_settings.screen_height / 2 * y))
                pic.blitme()
    tips.show_tips()
    # AI 自动选择
    if stats.ai_selecting:
        mouse_x, mouse_y = random_choice(sp_settings, stats)
        check_selected_picture(sp_settings, stats, st_chart, all_pictures,
                               selected_pictures, unselected_pictures,
                               optional_pictures, mouse_x, mouse_y)
    time.sleep(.01)
    pygame.display.flip()


def update_tips(tips):
    """更新提示信息"""
    # 显示提示信息
    tips.prep_remains()
    tips.prep_help()
    tips.prep_tips()
    tips.prep_select_count()


def update_charts(st_chart):
    """更新图表"""
    st_chart.prep_shapes()
    st_chart.prep_colors()
    st_chart.prep_sizes()
    st_chart.prep_quadrants()


def save_selections(stats, st_chart, user_name):
    """保存统计信息"""
    # stats.is_saved = False
    st_chart.save_to_file(user_name + '.txt')
    stats.is_saved = True


def clear_history(st_chart, user_name):
    """清空历史记录"""
    st_chart.clear_history(user_name + '.txt')

