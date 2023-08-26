from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.color("Green")


for num_sides in range(3,11):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)







screen = Screen()
screen.exitonclick()