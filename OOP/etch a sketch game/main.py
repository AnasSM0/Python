from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

def move_forwards():
    tom.forward(10)
def move_backwards():
    tom.backward(10)
def turn_Clockwise():
    tom.left(10)
def turn_AntiClockwise():
    tom.right(10)

def clear_drawing():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=turn_Clockwise)
screen.onkey(key="d",fun=turn_AntiClockwise)
screen.onkey(key="c",fun=clear_drawing)
screen.exitonclick()

