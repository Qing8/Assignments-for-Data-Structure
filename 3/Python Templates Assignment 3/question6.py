import turtle


def draw_tree(branchLen,t):
    '''
    @branchLen: Length of this branch. Should reduce every recursion. Starting length is 100.
    @t: Instance of turtle module. We can call turtle functions on this parameter.

    Figure out the tree pattern, and display the recursion tree.
    You may have to play/tune with angles/lengths to draw a pretty tree.

    @return: Nothing to return
    '''
    if branchLen < 10:
        return 
    
    
    else:
        t.forward(branchLen)
        
        t.left(30)
        draw_tree(branchLen-15,t)
        
        t.right(60)
        draw_tree(branchLen-15,t)
        t.left(30)
        
        t.backward(branchLen)
        
def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.backward(100)
    t.color("green")
    draw_tree(100,t)
    myWin.exitonclick()

main()
