class LeakyStack():
    def __init__(self, max_size):
        self._data = [None] * max_size   # Static size
        self._size = 0    # Track current number of elements
        self._top = 0  # Use this variable to make the stack circular


    def push(self, e):  # O(1)
#        pass
        self._size += 1
        self._data[self._top] = e
        self._top = (self._top+1) % len(self._data)

    def pop(self):      # O(1)
#        pass
        to_return = self._data[(self._top-1+len(self._data))%len(self._data)]
        self._top = (self._top-1+len(self._data))%len(self._data)
        return to_return

    def __len__(self):  # O(1)
#        pass
        return len(self._data)

    def is_empty(self): # O(1)
#        pass
        return len(self._data) == 0

    def __str__(self):  # O(n) or O(1) up to you
#        pass
        return str(self._data)
        


##############TEST CODES#################
#''' Comment out the test code if you are grading on gradescope.'''
#leakystack = LeakyStack(5)  # Max size = 5 stack.
#leakystack.push('a')
#leakystack.push('b')
#leakystack.push('c')
#print(leakystack)   # top of stack --> c b a
#leakystack.push('d')
#leakystack.push('e')
#print(leakystack)  # top of stack --> e d c b a 
#leakystack.push('f')
#print(leakystack)   # top of stack --> f e d c b,   a is gone because it is the oldest.
#print(leakystack.pop())  # f popped
#print(leakystack.pop())  # e popped
