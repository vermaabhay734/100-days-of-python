from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.color("Green")


for i in range(20):
    if i%2 == 0:
        tim.right(90)
    tim.forward(20)
    tim.penup()
    tim.forward(20)
    tim.pendown()





screen = Screen()
screen.exitonclick()