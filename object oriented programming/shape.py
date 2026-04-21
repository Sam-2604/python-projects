# Part 4 — Inheritance and Operator Overloading
# Build a Shape base class and two subclasses:

# Shape.__init__ takes color — __str__ returns "A [color] shape"
# Rectangle(Shape) — takes color, width, height — area() method — __str__ returns "A [color] rectangle: [width]x[height], area [area]"
# Circle(Shape) — takes color, radius — area() method using math.pi — __str__ returns "A [color] circle: radius [radius], area [area]" formatted to 2 decimal places
# Overload + on Rectangle — adding two rectangles returns a new Rectangle with same color, combined width, same height

import math

class Shape:
    def __init__(self, color):
        self.color = color
        
    def __str__(self):
        return f"A {self.color} shape"

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"A {self.color} rectangle: {self.width}x{self.height}, area {self.area():.2f}"
    
    def area(self):
        return self.width * self.height
    
    def __add__(self, other):
        return Rectangle(self.color, self.width + other.width, self.height)
    
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
        
    def __str__(self):
        return f"A {self.color} circle: radius {self.radius}, area {self.area():.2f}"
    
    def area(self):
        return math.pi * self.radius * self.radius
    
def main():
    x = Rectangle("blue", 2, 3)
    y = Rectangle("purple", 3, 4)
    z = Circle("red", 2)
    print(x)
    print(y)
    print(z)
    print(x + y)
    
if __name__ == "__main__":
    main()    
    

    
