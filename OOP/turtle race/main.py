from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500,height=400)

colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [-70,-40,-10,20,50,80]
all_turtles = []

for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)

def race():
    is_race_on = True
    while is_race_on:
        for turtle in all_turtles:
            random_distance = randint(0,10)
            turtle.forward(random_distance)
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
            

user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win " \
"the race? Enter a color: ")

if user_bet:
    race()

screen.exitonclick()