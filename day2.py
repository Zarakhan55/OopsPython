class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s1 = Student("John", "A")
s2 = Student("Sara", "B")

print(s1.name, s1.grade)   # John A
print(s2.name, s2.grade)   # Sara B






# Your Task

# Make a Book class with title, author, and price. Then:

# Create 3 books.
# Print each book’s details in a nice sentence, like: Python Basics by John costs $20

# class Book:
#     def __init__(self,title,author,price):
#         self.title = title
#         self.author = author
#         self.price = price
# b1=Book("Python Basics", "John", 20)
# b2=Book("Java Fundamentals", "Sara", 25)
# b3=Book("C++ Essentials", "Ali", 30)
# print(f"{b1.title} by {b1.author} costs ${b1.price}")
# print(f"{b2.title} by {b2.author} costs ${b2.price}")
# print(f"{b3.title} by {b3.author} costs ${b3.price}")

