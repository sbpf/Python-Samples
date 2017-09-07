import turtle

def draw_square():

    window = turtle.Screen()
    window.bgcolor("green")
    sinpri = turtle.Turtle()
    sinpri.shape("turtle")
    sinpri.color("yellow")
    sinpri.speed(2)

    count = 4
    while (count>0):
        sinpri.forward(100)
        sinpri.right(90)
        count = count-1
        
    window.exitonclick()

draw_square()


