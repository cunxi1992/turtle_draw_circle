## 1. 项目目标

画一个由正方形组成的圆，效果如下：

![艺术感的圆](/image/circle.gif)

## 2. 实现过程

要画一个由正方形组成的圆，需要先画一个正方形，下面让我们先来创建这个正方形。

### 2.1 先画一个正方形

我在纸上是如何画一个正方形的呢？一共四个步骤：

① 画一条横线；

② 右转90度；

③ 画一条横线；

④ 右转90度；

⑤ 画一条横线；

⑥ 右转90度；

⑦ 画一条横线；

⑧ 右转90度。

即 重复执行 ①和②。一看就知道要使用for循环了，一共四次循环。

新建一个Python文件，将其命名为mindstorms.py。接着在这个文件内创建一个函数 draw_square( )。Python中有一个模块叫turtle(意为乌龟)，它可以在屏幕上进行画画，至于为什么叫乌龟，可以到Python官方文档看一下，下面看具体的代码：

```
# -*- coding:utf-8 -*-
import turtle
def draw_square():
    # 添加一个窗口屏幕，即 画布
    window = turtle.Screen()
    # 设定画布的颜色为红色
    window.bgcolor("red")

    # 初始化对象，即对象brad具备了画画的能力
    brad = turtle.Turtle()
    # 设定想要前进的距离
    brad.forward(100)
    # 向右方转90度
    brad.right(90)

    # 设定任意时刻都可以关闭这个画画，点击屏幕即关闭
    window.exitonclick()

# 调用函数
draw_square()
```

执行上述代码，我们得到一个红色背景的窗口，还有一个叫brad的乌龟，其从屏幕中心向前移动了100个像素：

![向前移动100像素](/image/forward_100px.gif)

我们画好了之前第①和②两步，要画正方形，只要使用一个for循环，循环4次即可得到想要的正方形：

```
# -*- coding:utf-8 -*-
import turtle
def draw_square():
    # 添加一个窗口屏幕，即 画布
    window = turtle.Screen()
    # 设定画布的颜色为红色
    window.bgcolor("red")
    # 初始化对象，即对象brad具备了画画的能力
    brad = turtle.Turtle()
    for i in range(1,5):
        # 设定想要前进的距离
        brad.forward(100)
        # 向右方转90度
        brad.right(90)

    # 设定任意时刻都可以关闭这个画画，点击屏幕即关闭
    window.exitonclick()

# 调用函数
draw_square()
```

执行以上代码，我们画出了一个正方向，效果如下：
![正方形](/image/square.gif)

对于乌龟brad你可以自定义它的形状、颜色、速度，比如，我们真的把它的形状改成乌龟，颜色改成黄色，并将其速度改的更快一些：

```
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

    for i in range(1,5):
        # 设定想要前进的距离
        brad.forward(100)
        # 向右方转90度
        brad.right(90)

    # 设定任意时刻都可以关闭这个画画，点击屏幕即关闭
    window.exitonclick()

# 调用函数
draw_square()
```

执行上述代码，我们得到了如下效果：
![改变颜色和形状的正方形](/image/square_other.gif)


### 2.2 用正方形画圆

我们已经画出了正方形，接着用正方形组成一个圆怎么画呢？先观察一下用正方形画圆的规律，每一个正方形与上一个正方形的夹角为10度，因此，我们只需要让brad每次画完一个正方形后右转10度继续画正方形，直到右转了360度为止。

每次画完一个正方形后，右转10度，继续画正方形，一个圆共360度，因此需要画36次，我们这里可以使用while循环：

```
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
```

执行上述代码，我们完成了项目目标，一个由正方形组成的圆，给自己鼓个掌：
![由正方形组成的圆](/image/circle.gif)

关于turtle更多的信息，请访问Python官网，地址：https://docs.python.org/3/library/turtle.html，可以尝试自己画其他的图形，例如：

① 如何画一个半径100像素的圆？

② 如何画一朵花？

③ 如何画一个三角形？

![画图练习](/image/practice.jpeg)

鼓励大家尝试，遇到问题时Google、查turtle文档。

