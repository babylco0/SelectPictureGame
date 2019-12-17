# 统计信息
import json

import cairosvg
import pygal
import pygame


class Statistic:
    """统计信息"""

    def __init__(self, sp_settings, screen):
        """初始化统计属性"""
        self.sp_settings = sp_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.chart_width = self.screen_rect.width / 2 - 50
        self.chart_height = self.screen_rect.height / 2 - 50
        self.shapes = {}
        self.shapes_history = {}
        for s in self.sp_settings.pic_shapes:
            self.shapes[s] = 0
            self.shapes_history[s] = 0
        self.colors = {}
        self.colors_history = {}
        for c in self.sp_settings.pic_colors:
            self.colors[c] = 0
            self.colors_history[c] = 0
        self.sizes = {}
        self.sizes_history = {}
        for s in self.sp_settings.pic_sizes:
            self.sizes[str(s)] = 0
            self.sizes_history[str(s)] = 0
        self.quadrants_history = {'1': 0, '2': 0, '3': 0, '4': 0}
        self.quadrants = {'1': 0, '2': 0, '3': 0, '4': 0}
        # 加载历史数据
        # self.load_history()
        # 图形统计图表
        self.shapes_image = None
        self.shapes_image_rect = None
        self.prep_shapes()
        # 颜色统计图表
        self.color_image = None
        self.color_image_rect = None
        self.prep_colors()
        # 尺寸统计图表
        self.size_image = None
        self.size_image_rect = None
        self.prep_sizes()
        # 位置（象限）统计信息
        self.quadrant_image = None
        self.quadrant_image_rect = None
        self.prep_quadrants()

    def prep_shapes(self):
        """渲染图形统计资料为图像
        并放置于屏幕右上"""
        names, counts, history_counts = [], [], []
        for shape in self.shapes:
            names.append(shape)
            if self.shapes_history:
                history_counts.append(self.shapes_history[shape])
            counts.append(self.shapes[shape])
        chart = pygal.StackedBar()
        chart.x_labels = names
        chart.add('History', history_counts)
        chart.add('Today', counts)
        chart.title = 'Statistic of Shapes'
        chart.render_to_file('tmp.svg')
        cairosvg.svg2png(url='tmp.svg', write_to='tmp.png',
                         output_width=self.chart_width, output_height=self.chart_height)
        self.shapes_image = pygame.image.load('tmp.png')
        self.shapes_image_rect = self.shapes_image.get_rect()
        self.shapes_image_rect.center = self.screen_rect.width * 3 / 4, self.screen_rect.height / 4 + 50

    def prep_colors(self):
        """渲染颜色统计资料为图像
        并放置于屏幕左下"""
        names, counts, history_counts = [], [], []
        for color in self.colors:
            names.append(color)
            if self.colors_history:
                history_counts.append(self.colors_history[color])
            counts.append(self.colors[color])
        chart = pygal.StackedBar()
        chart.x_labels = names
        chart.add('History', history_counts)
        chart.add('Today', counts)
        chart.title = 'Statistic of Colors'
        chart.render_to_file('tmp.svg')
        cairosvg.svg2png(url='tmp.svg', write_to='tmp.png',
                         output_width=self.chart_width, output_height=self.chart_height)
        self.color_image = pygame.image.load('tmp.png')
        self.color_image_rect = self.color_image.get_rect()
        self.color_image_rect.center = self.screen_rect.width / 4, self.screen_rect.height * 3 / 4

    def prep_sizes(self):
        """渲染尺寸统计资料为图像
        并放置于屏幕右下"""
        names, counts, history_counts = [], [], []
        for size in self.sizes:
            names.append(size)
            if self.sizes_history:
                history_counts.append(self.sizes_history[size])
            counts.append(self.sizes[size])
        chart = pygal.StackedBar()
        chart.x_labels = names
        chart.add('History', history_counts)
        chart.add('Today', counts)
        chart.title = 'Statistic of Sizes'
        chart.render_to_file('tmp.svg')
        cairosvg.svg2png(url='tmp.svg', write_to='tmp.png',
                         output_width=self.chart_width, output_height=self.chart_height)
        self.size_image = pygame.image.load('tmp.png')
        self.size_image_rect = self.size_image.get_rect()
        self.size_image_rect.center = self.screen_rect.width * 3 / 4, self.screen_rect.height * 3 / 4

    def prep_quadrants(self):
        """"渲染位置统计信息为图像
        并放置于屏幕左上"""
        names, counts, history_counts = [], [], []
        for quadrant in self.quadrants:
            names.append(quadrant)
            if self.quadrants_history:
                history_counts.append(self.quadrants_history[quadrant])
            counts.append(self.quadrants[quadrant])
        chart = pygal.StackedBar()
        chart.x_labels = names
        chart.add('History', history_counts)
        chart.add('Today', counts)
        chart.title = 'Statistic of Quadrants'
        chart.render_to_file('tmp.svg')
        cairosvg.svg2png(url='tmp.svg', write_to='tmp.png',
                         output_width=self.chart_width, output_height=self.chart_height)
        self.quadrant_image = pygame.image.load('tmp.png')
        self.quadrant_image_rect = self.quadrant_image.get_rect()
        self.quadrant_image_rect.center = self.screen_rect.width / 4, self.screen_rect.height / 4 + 50

    def show_statistics(self):
        """显示统计图表信息"""
        self.screen.blit(self.shapes_image, self.shapes_image_rect)
        self.screen.blit(self.color_image, self.color_image_rect)
        self.screen.blit(self.size_image, self.size_image_rect)
        self.screen.blit(self.quadrant_image, self.quadrant_image_rect)

    def save_to_file(self, path=None):
        """保存统计信息到文件"""
        if path is None:
            path = 'history.txt'
        new_shapes_data = {}
        if self.shapes_history:
            for shape in self.shapes:
                new_shapes_data[shape] = self.shapes[shape] + self.shapes_history[shape]
        else:
            new_shapes_data = self.shapes
        new_colors_data = {}
        if self.colors_history:
            for color in self.colors:
                new_colors_data[color] = self.colors[color] + self.colors_history[color]
        else:
            new_colors_data = self.colors
        new_sizes_data = {}
        if self.sizes_history:
            for size in self.sizes:
                new_sizes_data[size] = self.sizes[size] + self.sizes_history[size]
        else:
            new_sizes_data = self.sizes
        new_quadrants_data = {}
        if self.quadrants_history:
            for quadrant in self.quadrants:
                new_quadrants_data[quadrant] = self.quadrants[quadrant] + self.quadrants_history[quadrant]
        else:
            new_quadrants_data = self.quadrants
        data = {'shapes': new_shapes_data,
                'colors': new_colors_data,
                'sizes': new_sizes_data,
                'quadrants': new_quadrants_data}
        with open(path, 'w') as fp:
            json.dump(data, fp)

    def load_history(self, path=None):
        """记载历史记录"""
        if path is None:
            path = 'history.txt'
        try:
            with open(path, 'r') as fp:
                data = json.load(fp)
                if data:
                    self.shapes_history = data['shapes']
                    self.colors_history = data['colors']
                    self.quadrants_history = data['quadrants']
                    self.sizes_history = data['sizes']
        except FileNotFoundError:
            pass

    def clear_history(self, path=None):
        """清空历史记录"""
        if path is None:
            path = 'history.txt'
        try:
            self.shapes_history.clear()
            self.colors_history.clear()
            self.quadrants_history.clear()
            self.sizes_history.clear()
            data = {'shapes': self.shapes_history,
                    'colors': self.colors_history,
                    'sizes': self.sizes_history,
                    'quadrants': self.quadrants_history}
            with open(path, 'w') as fp:
                json.dump(data, fp)
        except FileNotFoundError:
            pass
