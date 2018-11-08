from queue import Full
from queue import Empty

    

class BoostQueue():
    
    DEFAULT_CAPACITY = 5          # moderate capacity for all new queues

    def __init__(self):
        self._data = [None] * BoostQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def boost(self, k): # O(k)
        '''
        @k: number of steps to boost. k is greater than zero.
        # moves the element from the back of the queue k steps forward.
        # If the queue is empty an exception is raised.
        # If k is too big (greater or equal to the number of elements in the queue) the last element will become the first.
        @return: Nothing to return
        '''
##        pass
#        if self.is_empty():
#            raise Empty("Queue is empty!")
#        else:
#            if k >= self._size-1:
#                
#                i = self._size-1
#                last = self._data[self._size-1]
#                for _ in range(self._size-1):
#                    self._data[i] = self._data[i-1]
#                    i-=1
#                self._data[i] = last
#                
#            else:
#                i = self._size-1
#                last = self._data[i]
#                for _ in range(k):
#                    self._data[i] = self._data[i-1]
#                    i-=1
#                self._data[i] = last

        if self.is_empty():
            Empty("Queue is empty!")
        else:
            last = (self._front+self._size-1) % len(self._data)
            last_ele = self._data[last]
#            print("last:",last)
#            print("last_ele:",last_ele)
#            print("self_size:",self._size)
            if k >= self._size:
                for _ in range(self._size-1):
#                    print("last1:",last)
                    self._data[last] = self._data[last-1+len(self._data) % len(self._data)]
                    last = (last-1+len(self._data)) % len(self._data)
                
                self._data[self._front] = last_ele
                
            elif k < self._size:

                for _ in range(k):
                    self._data[last] = self._data[(last-1+len(self._data)) % len(self._data)] 
                    last = (last-1+len(self._data)) % len(self._data)
                self._data[(self._front + self._size-k-1)%len(self._data)] = last_ele
                



    def enqueue(self, e):
        if (self.is_full()):
            raise Full()
        self._data[(self._front + self._size) % len(self._data)] = e 
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty()
        to_return = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1 ) % len(self._data)
        self._size -= 1
        return to_return

    def first(self):
        if (self.is_empty()):
            raise Empty()
        return self._data[self._front]

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return (self._size == len(self._data))

    def __str__(self):
        return str(self._data)

##############TEST CODES#################
#''' Comment out the test code if you are grading on gradescope.'''
#queue = BoostQueue()
#queue.enqueue('a')
#queue.enqueue('b')
#print(queue)
#queue.enqueue('c')
#queue.enqueue('d')
#queue.eqqueue("m")
##queue.enqueue('e')
#print(queue)    # a b c d e
#queue.boost(2)  # boost e by 3
#print(queue)    # a e b c d
