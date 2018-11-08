class SharedMemoryStack():
    '''
    Design two stacks that share the same Python list, self._data.
    Both stacks can grow independently;

    no new item can be pushed in either stack when self._data is full.
    '''

    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * SharedMemoryStack.DEFAULT_CAPACITY
        self.stack1_size = 0
        self.stack2_size = 0

    def pushStack1(self, e):
#        pass
        self._data[self.stack1_size] = e
        self.stack1_size += 1
    
    def pushStack2(self, e):
#        pass
        self._data[len(self._data) - self.stack2_size -1] = e
        self.stack2_size += 1

    def popStack1(self):
#        pass
        to_return = self._data[self.stack1_size-1]
        self.stack1_size -= 1
#        self.pushStack2(to_return)
        return to_return

    def popStack2(self):
#        pass
        to_return = self._data[len(self._data) - self.stack2_size]
        self.stack2_size -= 1
#        self.pushStack1(to_return)
        return to_return


    def is_full(self):
#        pass
        return len(self._data) == self.stack1_size + self.stack2_size

    def is_empty1(self):
#        pass
        return self.stack1_size == 0

    def is_empty2(self):
#        pass
        return self.stack2_size == 0

    def peekStack1(self):
#        pass
        return self._data[self.stack1_size-1]

    def peekStack2(self):
#        pass
        return self._data[len(self._data)-self.stack2_size-1]

    def __str__(self):
        result = []
        result.append("Stack 1: ")
        # Your code 1 to show stack 1
        for i in self._data[:self.stack1_size]:
            result.append(str(i))
            result.append(", ")
        result.append("Stack 2: ")
        # Your code 2 to show stack 2
        for i in self._data[::-1][:self.stack2_size]:
            result.append(str(i))
            result.append(", ")
        return "".join(result)


##############TEST CODES#################
''' Comment out the test code if you are grading on gradescope.'''
#stack = SharedMemoryStack()
#stack.pushStack1(1)
#stack.pushStack1(2)
#stack.pushStack1(3)
#stack.pushStack1(4)
#stack.pushStack1(5)
#stack.pushStack1(6)
#stack.pushStack1(7)
#stack.pushStack1(8)
#stack.pushStack1(9)
#stack.pushStack1(10)
#print(stack)  # Stack 1: 1, 2, 3, 4; Stack 2: 5, 6, 7, 8, 9, 10
#print("Popping: ", stack.popStack1())  # popped 4
#stack.pushStack2(4)
#stack.popStack1()
#stack.pushStack2(11) # Stack 1: 1, 2, 3; Stack 2: 5, 6, 7, 8, 9, 10, 11
#print(stack)
#
#print(11111111111111111111111111111111111)
#while (not stack.is_empty1()):
#    print(stack.popStack1())
#print(22222222222222222222222222222222222222)
#while (not stack.is_empty2()):
#    print(stack.popStack2())
#
