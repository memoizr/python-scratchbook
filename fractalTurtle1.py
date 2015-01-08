import turtle
import time

def tree(branchLen, t):
    time.sleep(2)
    if branchLen > 5:
        print(branchLen)
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)
    else:
        print "Done!"

def main():
    turtle.setup(400,400)
    t = turtle.Turtle()
    t.speed("slowest")
    t.shape("turtle")
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()
