from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=500, height=400)
screen.exitonclick()
user_bet = screen.textinput(title="Make your bet!",prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
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


initialise_turtle(red,-150,'red')
initialise_turtle(orange,-100,'orange')
initialise_turtle(yellow,-50,'yellow')
initialise_turtle(green,0,'green')
initialise_turtle(blue,50,'blue')
initialise_turtle(indigo,100,'indigo')
initialise_turtle(violet,150,'violet')



