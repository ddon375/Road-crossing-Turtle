from turtle import Turtle
forward = 25


class CrossingTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.starting_position()

    def starting_position(self):
        self.goto(0, -280)

    def move(self):
        self.forward(forward)
