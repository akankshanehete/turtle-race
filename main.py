from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!",prompt="Which turtle will win the race? Enter a color: ")
print("Your bet is: " +user_bet)
red = Turtle(shape="turtle")
orange = Turtle(shape="turtle")
yellow = Turtle(shape="turtle")
green = Turtle(shape="turtle")
blue = Turtle(shape="turtle")
indigo = Turtle(shape="turtle")
violet = Turtle(shape="turtle")


def initialise_turtle(turtle,y_coord,color):
    turtle.penup()
    turtle.color(color)
    turtle.goto(-230,y_coord)
    turtle.speed("slow")


initialise_turtle(red,-150,'red')
initialise_turtle(orange,-100,'orange')
initialise_turtle(yellow,-50,'yellow')
initialise_turtle(green,0,'green')
initialise_turtle(blue,50,'blue')
initialise_turtle(indigo,100,'indigo')
initialise_turtle(violet,150,'violet')

all_turtles = [red, orange, yellow, green, blue, indigo, violet]

if user_bet:
    is_race_on = True

while is_race_on == True:
    for turtle in all_turtles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() > 230:
            is_race_on = False
            print(turtle.color()[1] + " won the race!")
            if turtle.color()[1] == user_bet:
                print("You won the bet!")
            else:
                print("You lost the bet :(")




screen.exitonclick()



