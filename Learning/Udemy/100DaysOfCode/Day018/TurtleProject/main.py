import random
import turtle
from turtle import Turtle, Screen


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


screen = Screen()
turtle.colormode(255)

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("aquamarine")


def draw_square():
    for _ in range(4):
        my_turtle.forward(100)
        my_turtle.left(90)


# draw_square()

my_turtle_1 = Turtle()
my_turtle_1.shape("turtle")
my_turtle_1.color("red")


def draw_dashed_line():
    for _ in range(15):
        my_turtle_1.forward(10)
        my_turtle_1.penup()
        my_turtle_1.forward(10)
        my_turtle_1.pendown()


# draw_dashed_line()

my_turtle_2 = Turtle()


def draw_shape(num_side_n):
    angle = 360 / num_side_n
    for _ in range(num_side_n):
        my_turtle_2.forward(100)
        my_turtle_2.right(angle)


def draw_shape_common():
    for shape_side_n in range(3, 11):
        my_turtle_2.color(random_color())
        draw_shape(shape_side_n)


# draw_shape_common()

my_turtle_3 = Turtle()
my_turtle_3.pensize(15)
my_turtle_3.speed("fast")

direction = [0, 90, 180, 270]


def random_walk():
    for _ in range(100):
        my_turtle_3.color(random_color())
        my_turtle_3.forward(30)
        my_turtle_3.setheading(random.choice(direction))


# random_walk()

my_turtle_4 = Turtle()
my_turtle_4.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        my_turtle_4.color(random_color())
        my_turtle_4.circle(100)
        my_turtle_4.setheading(my_turtle_4.heading() + size_of_gap)


draw_spirograph(5)

screen.exitonclick()
