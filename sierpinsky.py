import turtle
import time

def drawTriangle(points, color, t):
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0],points[0][1]) # move to bottom left
    time.sleep(0.5)
    t.down()
    t.begin_fill()
    t.goto(points[1][0],points[1][1]) # move to top
    time.sleep(0.5)
    t.goto(points[2][0],points[2][1]) # move to bottom right
    time.sleep(0.5)
    t.goto(points[0][0],points[0][1]) # move to bottom left
    time.sleep(0.5)
    t.end_fill()

def getMid(p1,p2):
    return( (p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

def sierpinski(points,degree,t):
    colormap = ['blue','red','green','white','yellow','violet','orange']
    time.sleep(2)
    drawTriangle(points,colormap[degree],t)
    if degree > 0:
        sierpinski([points[0],
                getMid(points[0],points[1]),
                getMid(points[0],points[2])],
            degree-1,t)
        sierpinski([points[1],
                getMid(points[0],points[1]),
                getMid(points[1],points[2])],
            degree-1,t)
        sierpinski([points[2],
                getMid(points[2],points[1]),
                getMid(points[0],points[2])],
            degree-1,t)

def main():
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.speed("slowest")
    turtle.setup(400,400)
    points = [[-100,-50],[0,100],[100,-50]]
    sierpinski(points,2,t)
    screen.exitonclick()

main()

