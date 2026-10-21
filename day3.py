class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def introduce(self):
        print(f"Hi, I am {self.name}")

    def is_pass(self):
        return self.marks >= 40

s1 = Student("Sara", 75)
s1.introduce()          # Hi, I am Sara
print(s1.is_pass())     # True


# Your Task
# Make a Rectangle class with:
# __init__ taking width and height
# A method area() that returns width x height
# A method perimeter() that returns 2 x (width + height)
# Create 2 rectangles and print their area and perimeter.
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
r1 = Rectangle(5, 3)
r2 = Rectangle(10, 7)
print(f"Rectangle 1 - Area: {r1.area()}, Perimeter: {r1.perimeter()}")
print(f"Rectangle 2 - Area: {r2.area()}, Perimeter: {r2.perimeter()}")