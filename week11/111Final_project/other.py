# import turtle as T
# import random

# def tree(branch_len, turtle):
#     if branch_len > 3:
#         if 8 <= branch_len <= 12:
#             if random.randint(0, 2) == 0:
#                 turtle.color('snow')  
#             else:
#                 turtle.color('lightcoral')  
#             turtle.pensize(branch_len / 3)
#         elif branch_len < 8:
#             if random.randint(0, 1) == 0:
#                 turtle.color('snow')
#             else:
#                 turtle.color('lightcoral')  
#             turtle.pensize(branch_len / 2)
#         else:
#             turtle.color('sienna')  
# #             turtle.pensize(branch_len / 10) 
# #         turtle.forward(branch_len)
# #         a = 1.5 * random.random()
# #         turtle.right(20 * a)
# #         b = 1.5 * random.random()
# #         tree(branch_len - 10 * b, turtle)
# #         turtle.left(40 * a)
# #         tree(branch_len - 10 * b, turtle)
# #         turtle.right(20 * a)
# #         turtle.up()
# #         turtle.backward(branch_len)
# #         turtle.down()

# # def petal(num_petals, turtle):
# #     for i in range(num_petals):
# #         a = 200 - 400 * random.random()
# #         b = 10 - 20 * random.random()
# #         turtle.up()
# #         turtle.forward(b)
# #         turtle.left(0)
# #         turtle.forward(a)
# #         turtle.down()
# #         turtle.color('lightcoral')  
# #         turtle.circle(1)
# #         turtle.up()
# #         turtle.backward(a)
# #         turtle.right(0)
# #         turtle.backward(b)

# # def draw_flower():
# #     w = T.Screen()
# #     w.setup(800, 600)
# #     w.bgcolor('wheat')

# #     t = T.Turtle()
# #     t.hideturtle()
# #     t.speed(0)
# #     t.color('sienna')
# #     t.setposition(-250, -200)
# #     t.left(90)
# #     t.up()
# #     t.backward(150)
# #     t.down()
# #     tree(80, t)

# #     t2 = T.Turtle()
# #     t2.hideturtle()
# #     t2.speed(0)
# #     t2.color('lightcoral')
# #     petal(200, t2)

# # draw_flower()

# import turtle as T
# import random
# import time

# def get_flower():
#     # draw tree body(60,t)
#     def tree(branch, t):
#         time.sleep(0)
#         if branch > 3:
#             if 8 <= branch <= 12:
#                 if random.randint(0, 2) == 0:
#                     t.color('snow')  
#                 else:
#                     t.color('lightcoral')  
#                 t.pensize(branch / 3)
#             elif branch < 8:
#                 if random.randint(0, 1) == 0:
#                     t.color('snow')
#                 else:
#                     t.color('lightcoral')  
#                 t.pensize(branch / 2)
#             else:
#                 t.color('sienna')  
#                 t.pensize(branch / 10)
#             t.forward(branch)
#             a = 1.5 * random.random()
#             t.right(20 * a)
#             b = 1.5 * random.random()
#             tree(branch - 10 * b, t)
#             t.left(40 * a)
#             tree(branch - 10 * b, t)
#             t.right(20 * a)
#             t.up()
#             t.backward(branch)
#             t.down()
        
#     # falling petals
#     def petal(m, t):
#         for i in range(m):
#             a = 200 - 400 * random.random()
#             b = 10 - 20 * random.random()
#             t.up()
#             t.forward(b)
#             t.left(0)
#             t.forward(a)
#             t.down()
#             t.color('lightcoral')  
#             t.circle(1)
#             t.up()
#             t.backward(a)
#             t.right(0)
#             t.backward(b)

#     # drawing part
#     w = T.Screen()
#     w.tracer(0, 0)

#     w = T.Screen()
#     w.setup(800, 600)
#     w.bgcolor('wheat')

#     # create first turtle and draw a flower
#     t1 = T.Turtle()
#     t1.up()
#     t1.hideturtle()
#     t1.getscreen().tracer(5, 0)
#     t1.color('sienna')
#     t1.setposition(-250, -200)
#     t1.left(90)
#     t1.up()
#     t1.backward(150)
#     t1.down()
#     tree(80, t1)

#     # draw falling petals
#     t3 = T.Turtle()
#     t3.hideturtle()
#     t3.getscreen().tracer(5, 0)
#     t3.color('lightcoral')
#     petal(200, t3)

#     # exit on click
#     T.exitonclick()
# get_flower()


import turtle
import random
import time

def Tree(branch, t, depth):
    time.sleep(0.05)
    if depth > 0:
        t.pensize(branch / 5)
        t.color('brown')
        t.forward(branch)

        a = 20 * random.random() - 10
        b = 20 * random.random() - 10

        t.right(a)
        Tree(branch - 10, t, depth - 1)
        t.left(a + b)
        Tree(branch - 10, t, depth - 1)
        t.right(b)
        t.up()
        t.backward(branch)
        t.down()

t = turtle.Turtle()
t.getscreen().bgcolor("white")
t.speed(0)
t.setheading(90)
t.up()
t.goto(0, -250)
t.down()

Tree(100, t, 5)
time.sleep(6)
turtle.bye()


