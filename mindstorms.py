# -*- coding:utf-8 -*-
import turtle
def draw_square():
    # 添加一个窗口屏幕，即 画布
    window = turtle.Screen()
    # 设定画布的颜色为红色
    window.bgcolor("red")

    # 初始化对象，即对象brad具备了画画的能力
    brad = turtle.Turtle()
    # 改变形状
    brad.shape("turtle")
    # 改变颜色
    brad.color("yellow")
    # 改变速度
    brad.speed(2)

    temp = 10
    # 该循环在每次画完一个正方形后，右转10度
    while temp <= 360:
        for i in range(1,5):
            # 设定想要前进的距离
            brad.forward(100)
            # 向右方转90度
            brad.right(90)

        temp += 10
        # 右转10度
        brad.right(10)

    # 设定任意时刻都可以关闭这个画画，点击屏幕即关闭
    window.exitonclick()

# 调用函数
draw_square()
