# 配置文件


class Settings:
    """配置类"""

    def __init__(self):
        """初始化配置参数"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.pic_sizes = [200, 300]
        self.pic_colors = ['red', 'green', 'blue']  # , 'yellow', 'black', 'brown']
        self.pic_shapes = ['triangle', 'rectangle', 'circle']  # , 'cross', 'hline', 'vline']
        self.select_list_number = 3
