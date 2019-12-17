# 使用乌龟画图绘制各种图形并使用PIL转换为PNG格式图片
import turtle
from PIL import Image
import math


class TurtleDraw(turtle.Turtle):
    """绘制正三角形
    使用turtle绘制一个正三角形
    并用PIL转换为png格式存储
    """

    def __init__(self, file_name, rect_size, fill_color, shape_type):
        """初始化正三角形的属性
        file_name: 保存的名称
        rect_size: 图形占据正方形边长
        fill_color: 填充颜色
        shape_type: 图形样式
        """
        super().__init__()
        self.file_name = file_name
        self.rect_size = rect_size
        self.fill_color = fill_color
        self.shape_type = shape_type

    def generate(self):
        """生成正三角形"""
        if self.shape_type == 'triangle':
            self.draw_triangle()
        elif self.shape_type == 'rectangle':
            self.draw_rectangle()
        elif self.shape_type == 'circle':
            self.draw_circle()
        elif self.shape_type == 'cross':
            self.draw_cross()
        elif self.shape_type == 'hline':
            self.draw_line(self.rect_size / 3, self.rect_size)
        elif self.shape_type == 'vline':
            self.draw_line(self.rect_size, self.rect_size / 3)

    def draw_triangle(self):
        """绘制正三角形"""
        w = self.rect_size
        h = self.rect_size * math.sqrt(3) / 2
        self.hideturtle()  # 隐藏小乌龟
        self.screen.setup(width=w + 50, height=h + 50)  # 设置画布大小
        # 移动画笔到画布左下角
        self.penup()
        self.setpos(-w / 2, -h / 2)
        self.pendown()
        # 绘制三角形
        self.color('black', self.fill_color)
        self.begin_fill()
        for _ in range(3):
            self.forward(self.rect_size)
            self.left(120)
        self.end_fill()
        # 保存为eps文件
        self.getscreen().getcanvas().postscript(file="tmp.eps")
        # 使用PIL打开临时eps文件并转换为png文件
        Image.open("tmp.eps").save(self.file_name + '.png')
        self.clear()

    def draw_rectangle(self):
        """"绘制矩形"""
        w = self.rect_size
        h = self.rect_size
        self.hideturtle()  # 隐藏小乌龟
        self.screen.setup(width=w + 50, height=h + 50)  # 设置画布大小
        # 移动画笔到画布左下角
        self.penup()
        self.setpos(-w / 2, -h / 2)
        self.pendown()
        # 绘制
        self.color('black', self.fill_color)
        self.begin_fill()
        for _ in range(4):
            self.forward(self.rect_size)
            self.left(90)
        self.end_fill()
        # 保存为eps文件
        self.getscreen().getcanvas().postscript(file="tmp.eps")
        # 使用PIL打开临时eps文件并转换为png文件
        Image.open("tmp.eps").save(self.file_name + '.png')
        self.clear()

    def draw_circle(self):
        """绘制圆形"""
        w = self.rect_size
        h = self.rect_size
        self.hideturtle()  # 隐藏小乌龟
        self.screen.setup(width=w + 50, height=h + 50)  # 设置画布大小
        # 移动画笔到画布底部中央
        self.penup()
        self.setpos(0, -h / 2)
        self.pendown()
        # 绘制
        self.color('black', self.fill_color)
        self.begin_fill()
        self.circle(w / 2)
        self.end_fill()
        # 保存为eps文件
        self.getscreen().getcanvas().postscript(file="tmp.eps")
        # 使用PIL打开临时eps文件并转换为png文件
        Image.open("tmp.eps").save(self.file_name + '.png')
        self.clear()

    def draw_cross(self):
        """绘制十字架"""
        w = self.rect_size
        h = self.rect_size
        self.hideturtle()  # 隐藏小乌龟
        self.screen.setup(width=w + 50, height=h + 50)  # 设置画布大小
        # 移动画笔至十字架中心左上
        cross_side_length = w / 3
        self.penup()
        self.setpos(-cross_side_length / 2, cross_side_length / 2)
        self.pendown()
        # 绘制
        self.color('black', self.fill_color)
        self.begin_fill()
        for _ in range(4):
            self.left(90)
            self.forward(cross_side_length)
            self.right(90)
            self.forward(cross_side_length)
            self.right(90)
            self.forward(cross_side_length)
        self.end_fill()
        # 保存为eps文件
        self.getscreen().getcanvas().postscript(file="tmp.eps")
        # 使用PIL打开临时eps文件并转换为png文件
        Image.open("tmp.eps").save(self.file_name + '.png')
        self.clear()

    def draw_line(self, lw, lh):
        """绘制线条
        lw: 线条宽度
        lh: 线条高度
        """
        w = self.rect_size
        h = self.rect_size
        self.hideturtle()  # 隐藏小乌龟
        self.screen.setup(width=w + 50, height=h + 50)  # 设置画布大小
        # 移动画笔到画布左下角
        self.penup()
        self.setpos(-lw / 2, -lh / 2)
        self.pendown()
        # 绘制
        self.color('black', self.fill_color)
        self.begin_fill()
        for i in range(4):
            self.forward(lw if i % 2 == 0 else lh)
            self.left(90)
        self.end_fill()
        # 保存为eps文件
        self.getscreen().getcanvas().postscript(file="tmp.eps")
        # 使用PIL打开临时eps文件并转换为png文件
        Image.open("tmp.eps").save(self.file_name + '.png')
        self.clear()
