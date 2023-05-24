import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# W = forward
# s = back
# a = counter-clock
# d = clockwise
# c = clear

def move_forwards():
    tim.forward(50)


def move_backwards():
    tim.backward(50)


def move_counterclockwise():
    tim_position = tim.heading() + 10
    tim.setheading(tim_position)


def move_clockwise():
    tim_position = tim.heading() - 10
    tim.setheading(tim_position)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counterclockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=tim.reset)

screen.exitonclick()
