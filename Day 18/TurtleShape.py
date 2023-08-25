from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("Blue")

tom = Turtle()
tom.shape("turtle")
tom.color("red")


def Square():
    for i in range(4):
        timmy.forward(100)
        timmy.left(90)
        i += 1

    
def Triangle():
    for i in range(3):
        tom.forward(100)
        tom.left(120)
        i += 1

Square()
Triangle()


screen = Screen()
screen.exitonclick()