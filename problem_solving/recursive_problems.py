"""
file: turtle_recursive_problems.py
language: python3
author: rafid
"""

import turtle

def recursive_spiral(leng):
    if leng < 10:
        return

    turtle.forward(leng)
    turtle.left(90)
    recursive_spiral(leng*.95)


def recursive_tree(leng,layers=3,angle=30):
    if layers == 0:
        turtle.circle(10)
        return


    turtle.left(angle)
    turtle.forward(leng)
    lyrs = layers-1
    recursive_tree(leng*.6,layers=lyrs)


    # go back to initial pos
    turtle.backward(leng)
    turtle.right(angle)

    turtle.right(angle)
    turtle.forward(leng)
    recursive_tree(leng*.6,layers=lyrs)

    turtle.backward(leng)
    turtle.left(angle)


# A, B, C
def tower_of_hanoi(discs=6,start_tower="A",intermediate_tower="B",end_tower="C"):
    """
    Move discs from from one tower to another
    Discs on tower A need to move to Tower C

    Move all but last to tower B using tower C
        - Move to C
        - Move to B
    Move last to Tower C
    """
    if discs == 0:
        return

    tower_of_hanoi(discs=discs-1,start_tower=start_tower,intermediate_tower=end_tower,end_tower=intermediate_tower)
    print("Moving "+str(discs)+" from "+start_tower+" to "+end_tower)
    tower_of_hanoi(discs=discs-1,start_tower=intermediate_tower,intermediate_tower=start_tower,end_tower=end_tower)

def main():
    #recursive_spiral(100)
    # turtle.speed(0)
    #turtle.tracer(0,0)
    turtle.left(90)
    recursive_tree(100)
    #tower_of_hanoi(discs=4)
    turtle.mainloop()

if __name__ == '__main__':
    main()
