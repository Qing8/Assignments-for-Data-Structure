class Empty(BaseException):
    def __init__(self, message):
        self.message = message
        
class SingleLinkedList:

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element, next):      # initialize node's fields
            self._element = element               # reference to user's element
            self._next = next                     # reference to next node



    def __init__(self):
        """Create an empty linkedlist."""
        self._head = None
        self._size = 0


    def __len__(self):
        """Return the number of elements in the linkedlist."""
        return self._size

    def is_empty(self):
        """Return True if the linkedlist is empty."""
        return self._size == 0

    def top(self):
        """Return (but do not remove) the element at the top of the linkedlist.

        Raise Empty exception if the linkedlist is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        return self._head._element              # head of list


    def insert_from_head(self, e):
        """Add element e to the head of the linkedlist."""
        # Create a new link node and link it
        new_node = self._Node(e, self._head)
        self._head = new_node
        self._size += 1



    def delete_from_head(self):
        """Remove and return the element from the head of the linkedlist.

        Raise Empty exception if the linkedlist is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        to_return = self._head._element
        self._head = self._head._next
        self._size -= 1
        return to_return

    def __str__(self):
        result = []
        curNode = self._head
        while (curNode is not None):
            result.append(str(curNode._element) + "-->")
            curNode = curNode._next
        result.append("None")
        return "".join(result)

    def sameSame(self, otherlist):
        # @otherlist: the list comparing with self list.
        # Checks whether two lists contain the same elements in the same order
        # returns True if same, return False otherwise.

        # Example:
        # l1: head --> 5 --> 4 --> 2 --> None
        # l2: head --> 5 --> 4 --> 2 --> None
        # >>> l1.sameSame(l2)
        # >>> True

        # @return: True or False
        # To do
#        pass
        if len(self) != len(otherlist):
            return False
        else:
            element1 = self._head
            element2 = otherlist._head
            while element1 != None and element2 != None:
                if element1._element == element2._element:
                    element1 = element1._next
                    element2 = element2._next
                else:
                    return False
            return True

    def remove_all_occurance(self, value):
        # @value: the value we are trying to remove from the self list.
        # remove all occurance of value in linked list. Return nothing.
        # Example:
        # l1: head --> 5 --> 4 --> 2 --> 4 --> 1 --> 9 --> 4 --> None
        # >>> l1.remove_all_occurance(4)
        # l1 should become: head --> 5 --> 2 --> 1 --> 9 --> None
        # @return: Nothing

        # To do
#        pass
        element = self._head
        while element._element == value and element._next != None:
            self._head = element._next
            element = element._next
            self._size -= 1
            
        if element._next == None:
            
            if element._element == value:
                self._head = None
                self._size -= 1
                
            else:
                self._head = element
                
            
                
        while element != None and element._next != None:
            if element._next._element == value:
                
                element._next = element._next._next
                self._size -= 1
                
            element = element._next
            
        if element == None:
            return
        elif element._next == None:
            if element._element == None:
                self.delete_from_head()
        



    def reverse(self):
        # reverses self list.
        # Example:
        # head --> 1 --> 2 --> 3 --> 4 --> None
        # >>> l.reverse()
        # head --> 4 --> 3 --> 2 --> 1 --> None
        # @return: Nothing
        
        # To do   
#        pass
        temp = []
        
        while self._size > 0: 
            temp.append(self.delete_from_head())
            
        for i in temp:
            self.insert_from_head(i)
        

##############Comment out test code if submitting on gradescope#############
#print("-----------Testing sameSame-------------")
#l1 = SingleLinkedList()
#l2 = SingleLinkedList()
#for i in range(5):
#    l1.insert_from_head(i)
#    l2.insert_from_head(i)
#print("l1111111111111111:",l1)
#print("Is l1 sameSame l2? Your answer:", l1.sameSame(l2))   # True
#print()
#print("-----------Testing remove_all_occurance-------------")
#l1 = SingleLinkedList()
#for i in range(10):
#    l1.insert_from_head(6)
#print(l1)  # 6-->6-->6-->6-->6-->6-->6-->6-->6-->6-->None
#l1.remove_all_occurance(6)
#print(l1)  # None
#print()
#print("-----------Testing reverse-------------")
#l1 = SingleLinkedList()
#for i in range(10):
#    l1.insert_from_head(i)
#print(l1)  # 9-->8-->7-->6-->5-->4-->3-->2-->1-->0-->None
#l1.reverse()
#print(l1)  # 0-->1-->2-->3-->4-->5-->6-->7-->8-->9-->None

#ll1 =  [0,1,2,0,1,2,0,1,2,0]
#ll2 = [0,0,0,0,0,0,0,0,0,0,0]
##ll3 = [0]
#for i in ll2:
#    l1.insert_from_head(i)
#print("l1111111:",l1)
#l1.remove_all_occurance(0)
#print(l1)