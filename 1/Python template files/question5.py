import math   # need math.pi
class Shape:
    # No need to modify this class.
    def __init__(self, name):
        self.name = name

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, name, radius):
        # TO DO
        # Call super first
        super().__init__(name)
        self.radius = radius

    def compute_area(self):
        # TO DO
        # @return the area of this circle
        return math.pi*self.radius**2

    def compute_perimeter(self):
        # TO DO
        # @return the perimeter of this circle
        return 2*math.pi*self.radius

class Rectangle(Shape):
    def __init__(self, name, length, height):
        # TO DO
        # Call super first
        super().__init__(name)
        self.length = length
        self.height = height

    def compute_area(self):
        # TO DO
        # @return the area of this rectangle
        return self.height*self.length

    def compute_perimeter(self):
        # TO DO
        # @return the parimeter of this rectangle
        return 2*(self.height+self.length)
        
        
c = Circle("Moon", 15)
#print(c.compute_perimeter())
r = Rectangle("Block", 20, 10)
#print(r.compute_area())



