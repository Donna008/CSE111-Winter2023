import turtle as T
import random
import time

# 画樱花的躯干(60,t)
def Tree(branch, t):
    time.sleep(0)
    t.speed(0)
    if branch > 3:
        if 8 <= branch <= 12:
            if random.randint(0, 2) == 0:
                t.color('snow')  # 白
            else:
                t.color('lightcoral')  # 淡珊瑚色
            t.pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')  # 淡珊瑚色
            t.pensize(branch / 2)
        else:
            t.color('sienna')  # 赭(zhě)色
            t.pensize(branch / 10)  # 6
        t.forward(branch)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        Tree(branch - 10 * b, t)
        t.left(40 * a)
        Tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()
       

# 掉落的花瓣
def Petal(m, t):
    # t.setheading(0)
    for i in range(m):
        print(i)
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(0)
        t.forward(a)
        t.down()
        t.color('lightcoral')  # 淡珊瑚色
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(0)
        t.backward(b)

# def Petal(m, t):
#     t.setheading(0)
#     for i in range(m):
#         a = 200 - 400 * random.random()
#         b = 10 - 20 * random.random()
#         t.up()
#         t.forward(b)
#         if t.heading() <= 180:
#             t.left(0)
#         else:
#             t.right(0)
#         t.forward(a)
#         t.down()
#         t.color('lightcoral')  # 淡珊瑚色
#         t.circle(1)
#         t.up()
#         t.backward(a)
#         if t.heading() <= 180:
#             t.right(0)
#         else:
#             t.left(0)
#         t.backward(b)

        

# 绘图区域
w = T.Screen()
w.setup(800, 600)
w.bgcolor('wheat')  # wheat小麦

# 创建第一个 turtle，并画出樱花
t1 = T.Turtle()
t1.up()
t1.hideturtle()  # 隐藏画笔
t1.getscreen().tracer(5, 0)
t1.color('sienna')
t1.setposition(-250, -200)  # 设置 turtle 的起始位置
t1.left(90)
t1.up()
t1.backward(150)
t1.down()
Tree(80, t1)

# 创建第二个 turtle，并画出樱花
# t2 = T.Turtle()
# t2.hideturtle()  # 隐藏画笔
# t2.getscreen().tracer(5, 0)
# t2.color('sienna')
# t2.setposition(50, -200)  # 设置 turtle 的起始位置
# t2.left(90)
# t2.up()
# t2.backward(150)
# t2.down()
# Tree(80, t2)

# 绘制掉落的花瓣
t3 = T.Turtle()
t3.hideturtle()  # 隐藏画笔
t3.getscreen().tracer(5, 0)
t3.color('lightcoral')
Petal(200, t3)


