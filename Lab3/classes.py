class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

manipulator = StringManipulator()
manipulator.getString()
manipulator.printString()


class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

shape = Shape()
print("Area of Shape:", shape.area())  

square = Square(5)
print("Area of Square:", square.area()) 


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(4, 6)
print("Area of Rectangle:", rectangle.area()) 


import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates of the point: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

point1 = Point(1, 2)
point1.show()

point1.move(3, 4)
point1.show() 

point2 = Point(5, 6)
distance = point1.dist(point2)
print("Distance between two points:", distance)


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into account. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from account. New balance: {self.balance}")


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

numbers = [54, 23, 77, 32, 27, 98]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers:", prime_numbers)

account = Account("John Doe", 1000)
print(f"Account owner: {account.owner}, Balance: {account.balance}")

account.deposit(500)
account.withdraw(200)
account.withdraw(1500)

print(f"Final balance: {account.balance}")
