from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.go_home()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_reached_the_top(self):
        return self.ycor() > FINISH_LINE_Y

    def go_home(self):
        self.goto(STARTING_POSITION)
