from turtle import Turtle, Screen
import random
tim = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(5)
tim.speed("fastest")

for num_sides in range(200):
    tim.color(random.choices(colours))
    tim.forward(10)
    tim.setheading(random.choice(directions))







screen = Screen()
screen.exitonclick()