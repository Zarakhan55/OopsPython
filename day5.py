# class Student:
#     school = "ABC School"          # class variable, shared

#     def __init__(self, name):
#         self.name = name           # instance variable, different for each

# s1 = Student("Ali")
# s2 = Student("Sara")

# print(s1.name, s1.school)   # Ali ABC School
# print(s2.name, s2.school)   # Sara ABC School







# class Employee:
#     company = "TechCorp"            # shared

#     def __init__(self, name, salary):
#         self.name = name            # own
#         self.salary = salary        # own

#     def show(self):
#         print(self.name, self.salary, self.company)

# e1 = Employee("Ali", 5000)
# e2 = Employee("Sara", 6000)
# e3 = Employee("John", 5500)

# e1.show()
# e2.show()
# e3.show()

# Employee.company = "NewCorp"    # change for everyone

# e1.show()
# e2.show()
# e3.show()




class Product:
    shop_name = "MyShop"          # class variable, shared
    tax_ate = 0.1                 # class variable, shared
    total_products = 0                # class variable, shared
    def __init__(self, name, price):
        self.name = name           # instance variable, different for each
        self.price = price         # instance variable, different for each
        Product.total_products += 1  # increment total products
    def show(self):
        print(f"{self.name}: ${self.price} (Shop: {Product.shop_name}, Tax Rate: {Product.tax_ate})")

c1 = Product("Laptop", 1000)
c2 = Product("Phone", 500)
c3 = Product("Tablet", 300)

c1.show()
c2.show()
c3.show()

Product.total_products = 3
c1.show()
c2.show()
c3.show()