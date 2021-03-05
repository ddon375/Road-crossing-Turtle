from turtle import Turtle
import turtle
import random
turtle.colormode(255)

def rgb_color():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1, 255)
    return r, g, b

class Cars:
    def __init__(self, xpos, ypos):
        self.car_list = []
        self.create_cars(xpos, ypos)

    def create_cars(self, xcor, ycor):
        color = rgb_color()
        for i in range(3):
            my_turtle = Turtle()
            my_turtle.penup()
            my_turtle.color(color)
            my_turtle.shape("square")
            my_turtle.goto(xcor, ycor)
            xcor += 20
            self.car_list.append(my_turtle)

    def move_cars(self):
        for items in range(2, 0, -1):
            previous = self.car_list[items - 1].pos()
            self.car_list[items].goto(previous)
        self.car_list[0].setheading(180)
        self.car_list[0].forward(20)

