from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-295, 270)
        self.write_score()

    def write_score(self):
        self.write(f"level:{self.level} ", False, "left", ("courier", 16, "italic"))

    def increase_score(self):
        self.level += 1
        self.clear()
        self.write_score()