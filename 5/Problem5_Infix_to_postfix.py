# Use this stack to perform infix to postfix. No need to modify the stack class.
class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop(-1)

    def __repr__(self):
        return str(self._data)


def infix_to_postfix(string):
    '''
    @string: input infix expression string

    The Algorithm is described in the assignment instruction.

    @return: corresponding postfix expression string, 
             the string can include spaces, but spaces does not affect testing.
    '''
    stack = ArrayStack()
    tokens = string.split(" ")
#    print("tokens:",tokens)
    precedence = {"+":1, "-":1, "*":2, "/":2, "(":0, ")":0}
    # To do
#    pass
    to_return = ""
    stack = ArrayStack()
    for i in tokens:
        if i.isdigit() or i.isalpha():
            to_return += i
        else:
            if i == "(":
                stack.push(i)
                
            elif i == ")":
                while stack.top() != "(":
                    to_return += stack.pop()
                stack.pop()
            else:
                if stack.is_empty() or precedence[i] > precedence[stack.top()]:
                    stack.push(i)
                else:
                    while len(stack) > 0 and precedence[i] <= precedence[stack.top()]:
                        to_return += stack.pop()
                    stack.push(i)
    while len(stack) > 0 :
        if precedence[stack.top()] > 0:
            to_return += stack.pop()
        else:
            stack.pop()
    return to_return
            
            
                
                


##############TEST CODES#################
#''' Comment out the test code if you are grading on gradescope.'''
#print(infix_to_postfix("( 3 + 2 ) / 4 + ( 3 * 2 + 4 )")) # OUTPUTS: 3 2 + 4 / 3 2 * 4 + + 
#print(infix_to_postfix("X + Y / ( 5 * Z ) + 10"))  # OUTPUTS: X Y 5 Z * / + 10 + 
#print(infix_to_postfix("1 + ( 2 - 3 ) * 4 + 5 / 6 / 7"))
                                        
