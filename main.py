from turtle import Turtle, Screen
from cars import Cars
import time
import random
from crossing_turtle import CrossingTurtle
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.title("Turtle Crossing Game")
scoreboard = Scoreboard()
my_screen.tracer(0)


crossing_turtle = CrossingTurtle()
y_axis_list = []
for numbers in range(-240, 260, 20):
    y_axis_list.append(numbers)
x_axis_list = [300,320,340, 360]


my_screen.listen()
my_screen.onkey(crossing_turtle.move, "Up")

sleep = 0.5
many_cars = []
game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(sleep)
    chosen_x = random.choice(x_axis_list)
    chosen_y = random.choice(y_axis_list)
    if chosen_x != 340:
        cars = Cars(chosen_x, chosen_y)
        many_cars.append(cars)
    for items in many_cars:
        items.move_cars()
    for items in many_cars:
        for item in items.car_list:
            if crossing_turtle.distance(item) <= 20:
                game_is_on = False
    if crossing_turtle.ycor() >= 290:
        sleep *= 0.7
        crossing_turtle.starting_position()
        scoreboard.increase_score()

my_screen.exitonclick()
