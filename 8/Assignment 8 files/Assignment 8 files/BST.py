from LinkedQueue import *
from LinkedBinaryTree import *

class BinarySearchTree(LinkedBinaryTree):

    #------------------------------- nonpublic utilities -------------------------------
    def _subtree_search(self, p, v):
        """Return Position of p's subtree having value v, or last node searched."""
        if v == p.element():                                   # found match
            return p                                         
        elif v < p.element():                                  # search left subtree
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), v)   
        else:                                              # search right subtree
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), v)
        return p                                           # unsucessful search

    def _subtree_first_position(self, p):
        """Return Position of first item in subtree rooted at p."""
        walk = p
        while self.left(walk) is not None:                 # keep walking left
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        """Return Position of last item in subtree rooted at p."""
        walk = p
        while self.right(walk) is not None:                # keep walking right
            walk = self.right(walk)
        return walk
    
    #--------------------- public methods providing "positional" support ---------------------
    def first(self):
        """Return the first Position in the tree (or None if empty)."""
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        """Return the last Position in the tree (or None if empty)."""
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        """Return the Position just before p in the natural order.

        Return None if p is the first position.
        """
        self._validate(p)                            # inherited from LinkedBinaryTree
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            # walk upward
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p):
        """Return the Position just after p in the natural order.

        Return None if p is the last position.
        """
        self._validate(p)                            # inherited from LinkedBinaryTree
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above

    def find_position(self, v):
        """Return position with value v, or else neighbor (or None if empty)."""
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), v)
            return p

    def delete(self, p):
        """Remove the item at given Position."""
        self._validate(p)                            # inherited from LinkedBinaryTree
        if self.left(p) and self.right(p):           # p has two children
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())    # from LinkedBinaryTree
            p =  replacement
        # now p has at most one child
        parent = self.parent(p)
        self._delete(p)                              # inherited from LinkedBinaryTree
        self._rebalance_delete(parent)               # if root deleted, parent is None
            
    #--------------------- public methods for accessing/mutating ---------------------
    def get_position(self, v):
        """Return the Position associated with value (raise Error if not found)."""
        if self.is_empty():
            raise Empty('Tree is empty')
        else:
            p = self._subtree_search(self.root(), v)
            if v != p.element():
                raise Error('Not found: ' + repr(v))
            return p

    def insert(self, v):
        """Insert value v into the Binary Search Tree"""
        if self.is_empty():
            leaf = self._add_root(v)     # from LinkedBinaryTree
        else:
            p = self._subtree_search(self.root(), v)
            if p.element() < v:
                leaf = self._add_right(p, v)        # inherited from LinkedBinaryTree
            else:
                leaf = self._add_left(p, v)         # inherited from LinkedBinaryTree
        self._rebalance_insert(leaf)                 # hook for balanced tree subclasses

    def delete_value(self, v):
        """Remove Position within the Tree that contains value v (raise Error if not found)."""
        if not self.is_empty():
            p = self._subtree_search(self.root(), v)
            if v == p.element():
                self.delete(p)                           # rely on positional version
                return                                   # successful deletion complete
        raise Error('Not found: ' + repr(v))


    def _rebalance_insert(self, p):     # Do nothing in BST, going to be overidden in AVLTree.
        pass

    def _rebalance_delete(self, p):     # Do nothing in BST, going to be overidden in AVLTree.
        pass

    def __iter__(self):
        """Generate an iteration of all values in order."""
        p = self.first()
        while p is not None:
            yield p.element()
            p = self.after(p)

    def __reversed__(self):
        """Generate an iteration of all values in reverse order."""
        p = self.last()
        while p is not None:
            yield p.element()
            p = self.before(p)

    
    



    #-------------------------- Assignment 8 functions --------------------------

    def iterative_search(self, p, v):
        ''' 
        @p: a Position within self Tree.
        @v: the value we are searching for.

        Return Position of p's subtree having value v, or last Position searched. 

        @return: the Position that contains value v, or last Position searched.
        '''
        # Task 1
        self.get_position()
    
    
    def get_kth_largest(self, k):
        ''' 
        @k: integer, k-th largest.

        return the Position of k-th largest node within self Tree.
        
        @return: Position of kth largest node.
        '''
        # Task 2
        pass
    
    def LCA(self, p1, p2):
        ''' 
        @p1: first Position within self Tree
        @p2: second Position within self Tree

        return the Position of the lowest common ancestor node.

        @return: the Position of the lowest common ancestor node
        '''
        
        # Task 3
        pass
    





    #-------------------------- end of Assignment 8 functions --------------------------


#-------------------------- Flip booleans to enable testing --------------------------
problem1 = False
problem2 = False
problem3 = False

#-------------------------- Problem 1 tests... --------------------------
if (problem1):
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(2)
    bst.insert(7)
    bst.insert(12)
    bst.insert(18)

    #   10       
    #  / \   
    # /   \  
    # 5   15   
    #/ \ / \ 
    #2 7 12 18 

    print("Testing problem 1 iterative_search... searching for 5")
    print(bst.iterative_search(bst.root(), 5).element(), ", should be 5")  
    print("Testing problem 1 iterative_search... searching for 12")
    print(bst.iterative_search(bst.root(), 12).element(), ", should be 12")  
    print("Testing problem 1 iterative_search... searching for 8")
    print(bst.iterative_search(bst.root(), 8).element(), ", should be 7")  

#-------------------------- Problem 2 tests... --------------------------
if (problem2):
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(2)
    bst.insert(7)
    bst.insert(12)
    bst.insert(18)
    #   10       
    #  / \   
    # /   \  
    # 5   15   
    #/ \ / \ 
    #2 7 12 18 
    print("Testing problem 2 find k-th largest... 3rd largest is")
    print(bst.get_kth_largest(3).element(), ", should be 12")
    print("Testing problem 2 find k-th largest... 7th largest is")
    print(bst.get_kth_largest(7).element(), ", should be 2")
    print("Testing problem 2 find k-th largest... 9th largest is")
    print(bst.get_kth_largest(9).element(), ", should be 2")



if (problem3):
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(20)
    bst.insert(6)
    bst.insert(9)

    pos_6 = bst.get_position(6)
    pos_9 = bst.get_position(9)
    pos_7 = bst.get_position(7)
    pos_3 = bst.get_position(3)
    pos_20 = bst.get_position(20)
    print(bst.LCA(pos_6, pos_9).element(), "    Expected result is 7")
    print(bst.LCA(pos_6, pos_7).element(), "    Expected result is 7")
    print(bst.LCA(pos_3, pos_20).element(), "    Expected result is 10")

