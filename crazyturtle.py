import turtle

turtle.setup(400,400)

t = turtle.Turtle()
t.shape("turtle")
t.speed("slowest")

def turtleSquare(size):
  t.left(90)
  t.forward(size)
  t.left(90)
  t.forward(size)
  t.left(90)
  t.forward(size)
  t.left(90)
  t.forward(size)
  
turtleSquare(200)
  