import random
import turtle

turtle.tracer(False)                          # skips the drawing animation

turtle.Screen().bgcolor("light blue")         #sets the background color
turtle.speed(30)                              #sets the drawing speed

def filled_circle(radius, color):             #draws a filled circle
    turtle.color(color,color)
    turtle.begin_fill()
    turtle.circle(radius)                     #draws circle according to set radius
    turtle.end_fill()

def cloud(radius, cloud_color="white"):

    randomNum = 0                             #define a random number variable, set to 0

    for i in range(8):                        #repeat function 8 times 
                                              #this first section
        turtle.penup()                        #lifts pen up so to not draw a line
        if (i%2 == 1):                        #% returns the remainder of i/2, checks if num odd
            turtle.right(90)                  #rotates right 90 degrees
            turtle.forward(randomNum)         #moves "forward"(down) a randomly generated amount
            turtle.left(90)                   #rotates left 90 degrees (resetting it)
        else:                                 #otherwise, if number is even
            turtle.left(90)                   #rotates left 90 degrees
            turtle.forward(randomNum)         #moves "forward"(up) a randomly generated amount
            turtle.right(90)                  #rotates right 90 degrees (resetting it)
        turtle.pendown()                      #puts pen down in new spot
                                              #this section resets
        filled_circle(radius,cloud_color)     #prints a circle

        turtle.penup()                        #lifts pen up
        turtle.forward(random.randint(2,10))  #moves forward a randomly generated int between 2 and 10
        randomNum = random.randint(4,8)       #sets randomNum variable to randomly generated int between 4 and 8
        if (i%2 == 0):                        #% returns the remainder of i/2
            turtle.right(90)
            turtle.forward(randomNum)
            turtle.left(90)
        else:
            turtle.left(90)
            turtle.forward(randomNum)
            turtle.right(90)
        turtle.pendown()

radius = 11                                   #radius of circle        

def cloudy_sky():
    for i in range(18):
        cloud(radius)
        turtle.penup()
        turtle.goto(random.randint(-300,300),random.randint(-300,300))
        turtle.pendown()

def curve():
    for i in range(45):
        turtle.right(1)
        turtle.forward(1)

def bird():
    turtle.pensize(3)
    turtle.penup()
    turtle.pencolor("black")
    turtle.goto(-200,30)
    turtle.pendown()
    turtle.begin_fill()
    curve()
    turtle.left(90)
    curve()


cloudy_sky()
bird()

turtle.done()

