1
# class Teacher():

#     def __init__(self, full_name, subject, experience=0):

#         self.full_name = full_name
#         self.subject = subject
#         self.experience = experience


#     def teach(self):
#         return f"{self.full_name} is teaching {self.subject}"

#     def set_experience(self, year):
#         if year > 0:
#             self.experience = year
#         else:
#             print("Experince cant be accepted!")

#     def get_experience(self):
#         return f"Experience: {self.experience} year"



# teacher1 = Teacher("Nasiba Karimova",  "Python")
# teacher1.set_experience(6)

# print(teacher1.teach())
# print(teacher1.get_experience())



2
# class Student():

#     school_name = "School 21"
#     def __init__(self,name , grade):
#         self.name = name
#         self.grade = grade

#     def show_info(self):
#         return f"{self.name} | {self.grade} | {Student.school_name}"



# std =  Student("Ali", 10)
# std2 = Student("Sara", 11)
# print(std.show_info())
# print(std2.show_info())

# Student.school_name = "Python academy"
# print(std.show_info())
# print(std2.show_info())


3
# class Employee:

#     employees_count = 0
#     def __init__(self, name, work):
#         self.name = name
#         self.work = work
#         self.employees_count += 1

#     def show_info(self):
#         return f"{self.name} | {self.work}"

#     @classmethod
#     def get_count(cls):
#         return cls.employees_count

# worker1 = Employee("Ali", "Developer")
# worker1 = Employee("Sara", "Designer")
# worker1 = Employee("Rustam", "Manager")


# print(f"Total employee: {Employee.get_count()}")

    






4
# class Calculator:

#     @staticmethod
#     def add(a, b):
#         return a+b

#     @staticmethod
#     def sub(a, b):
#         return a-b

#     @staticmethod
#     def mul(a, b):
#         return a*b

#     @staticmethod
#     def div(a, b):
#         try:
#             return a/b
#         except ZeroDivisionError:
#             return "Cannot divide by zero"

# print(Calculator.add(12, 3))
# print(Calculator.mul(12, 3))
# print(Calculator.sub(12, 3))
# print(Calculator.div(12, 3))



5
# class Currency:
#     usd_rate = 10.90

#     def __init__(self, usd):
#         self.usd = usd

#     def to_somoni(self):
#         return self.usd_rate * self.usd

#     @staticmethod
#     def valid_rate(value):
#         return value > 0


#     @classmethod
#     def change_rate(cls, new_rate):
#         if cls.valid_rate(new_rate):
#             cls.usd_rate = new_rate
#             return True
        
#         return False




# dd = Currency(100)
# print(f"Before: {dd.to_somoni()} TJS")
# print(f"Rate changed: {Currency.change_rate(11.20)}")
# print(f"After: {dd.to_somoni()}")



6
# class BankAccount():

#     def __init__(self, owner, balance=0):

#         self.owner = owner
#         self.balance = balance


#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount


#     def withdraw(self, amount):

#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient funds")


#     def __str__(self):
#         return f"Owner: {self.owner}, Balance: {self.balance}"


# user = BankAccount("Alice", 1000)
# user.deposit(500)
# print(user)
# user.withdraw(2000)
# print(user)
# user.withdraw(200)
# print(user)


7

# class Product():

#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def __str__(self):
#         return f"{self.name} -- {self.price} TJS, stock: {self.quantity}"

#     def __repr__(self):
#         return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"


# pr = Product("Laptop", 7500, 3)
# print(pr)
# print(pr.__repr__())
    



8
# class Book:
#     clasc = "book_class"
#     def __init__(self, title, author, isbn):

#         self.title = title
#         self.author = author
#         self.isbn = isbn

#     def __eq__(self, value):
#         if not isinstance(value, Book):
#             return False
#         return self.isbn == value.isbn
       

    
#     def __repr__(self):
#         return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

# book1 = Book("Python101", "Ali", "978-1")
# book2 = Book("PythonBasics", "Sara", "978-1")
# book3 = Book("Django101", "Rustam","978-2")
# print(f"book1 == book2: {book1.__eq__(book2)}")
# print(f"book1 == book3: {book1.__eq__(book3)}")
# print(f"book1 == '978-1': {book1.__eq__("978-1")}")

# print(book1.__repr__())



9
# class Playlist:

#     def __init__(self, name):
#         self.playlist = []
#         self.name = name

#     def add_song(self, song:str):
#         self.playlist.append(song.capitalize())

#     def __len__(self):
#         return len(self.playlist)

#     def __contains__(self, song):
#         return song.capitalize() in self.playlist



# s = Playlist("Study") 
# s.add_song("Believer")
# s.add_song("Numb")
# s.add_song("imagine")
# s.add_song("jazz")
# s.add_song("halo")
# print(f"{s.name}: {s.__len__()} songs")
# print(f"numb found: {s.__contains__("numb")}")
# print(f"jazz found: {s.__contains__("JAZz")}")
# print(f"Halo found: {s.__contains__("halo")}")


10
# class Vector:

#     def __init__(self,name, x, y):
#         self.name = name
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         print(f"Sum: ({self.x + other.x}, {self.y + other.y})")
#         print(f"Originals unchanged: ({self.x}, {self.y}), ({other.x}, {other.y})")

#     def __str__(self):
#         return f"{self.name}: ({self.x}, {self.y})"


# vect1 = Vector("vector1", 2, 5)
# vect2 = Vector("vector2", 3, -1)

# print(vect1)
# print(vect2)
# vect1.__add__(vect2)