# 图片状态类


class PicturesStats:
    """"图片状态类"""

    def __init__(self, remains):
        """初始化图片状态类属性"""
        self.remains = remains
        self.tips_help_str = 'Click image to select...'
        self.tips_tip_str = 'LSHIFT to show statistic...ENTER to save...ESC to exit...'
        self.ai_selecting = False
        # 选择列表
        self.select_list = []
        # 显示统计信息
        self.show_statistic = False
        # 数据保存标识
        self.is_saved = False
