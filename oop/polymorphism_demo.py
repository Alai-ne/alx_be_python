import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")
    class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2
     # Example usage:
# Create a list of shapes
shapes = [Rectangle(10, 5), Circle(7)]

# Iterate over the list and call the area method
for shape in shapes:
    print(f"The area is: {shape.area()}")
