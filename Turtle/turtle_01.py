# Call turtle module
import turtle

# Create a varible for the "arrow"  
arrow = turtle.Turtle() # shape is the "arrow" form

arrow.color("black", "#3260F6") # or only type the color

arrow.begin_fill() # "begin_fill" is a function for the beginning of the fill
arrow.forward(100) # "forward" is the forward distance

arrow.left(90), arrow.forward(100) # "left" is the angle to up

arrow.right(-90), arrow.forward(100) # "right" is the angle to down

arrow. right(-90), arrow.forward(100)

arrow.penup()
arrow.forward(150) # "forward" with "penup" and "pendown" are for the pen go a certain distance
arrow.pendown()

arrow.forward(100) # "forward" is the forward distance

arrow.left(90), arrow.forward(100) # "left" is the angle to up

arrow.right(-90), arrow.forward(100) # "right" is the angle to down

arrow. right(-90), arrow.forward(100)
arrow.end_fill() # "end_fill" is a function for the end of the fill

turtle.done()
