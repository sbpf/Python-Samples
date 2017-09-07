import turtle

def draw_shapes():

    window = turtle.Screen()
    window.bgcolor("green")

    #a yellow turtle drawing a square
    rachel = turtle.Turtle()
    rachel.shape("turtle")
    rachel.color("yellow")
    
    square_count = 36
    while (square_count>0):
        count = 4        
        while (count>0):
            rachel.forward(100)
            rachel.right(90)
            count = count-1
            
        rachel.right(10)   
        square_count = square_count-1
    
    
    window.exitonclick()

draw_shapes()
