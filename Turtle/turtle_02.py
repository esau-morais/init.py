import turtle

arrow2 = turtle.Turtle()

arrow2.color("blue", "black")

arrow2.speed(5)

arrow2.begin_fill()
for i in range(25):
    arrow2.forward(300)
    arrow2.left(165)
arrow2.end_fill()

turtle.done()
