import turtle

def draw_shapes():

    window = turtle.Screen()
    window.bgcolor("green")

    #a yellow turtle drawing a square
    square = turtle.Turtle()
    square.shape("turtle")
    square.color("yellow")
    square.speed(5)

    count = 4
    while (count>0):
        square.forward(100)
        square.right(90)
        count = count-1      
  
    #a red turtle drawing a circle
    circle = turtle.Turtle()
    circle.shape("turtle")
    circle.color("red")
    circle.speed(5)
    circle.circle(100)

    #a blue turtle drawing a triangle
    triangle = turtle.Turtle()
    triangle.shape("turtle")
    triangle.color("blue")
    triangle.speed(5)

    count = 3
    while (count>0):
        triangle.right(120)
        triangle.forward(100)
        count = count -1
    
    window.exitonclick()
  
draw_shapes()




