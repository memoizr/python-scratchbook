var = 0
def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    global var
    var += 1
    print("moving disk from", fp, "to", tp)

def main():
    moveTower(3,"A","B","C")

main()
