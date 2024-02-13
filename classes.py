import math
#1
class MyClass():
    def __init__(self):
        self.input_string = ""
    def getString(self):
        self.input_string = input()
    def printString(self):
        print(self.input_string.upper())

#2
class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length * self.length
#3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.width * self.length
#4
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print("({}, {})", format(self.x,self.y))
    def move(self,new_x, new_y):
        self.x = new_x
        self.y = new_y
    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

#5
class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit of ${} successful. New balance: ${}".format(amount, self.balance))
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawal of ${} successful. New balance: ${}".format(amount, self.balance))
        else:
            print("Invalid withdrawal amount or insufficient funds.")


'''acc = Account("Nurbek", 0)
acc.deposit(500)
acc.withdraw(250)'''

#6
'''def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

prime_numbers = list(filter(lambda x : is_prime(x), numbers))

print(prime_numbers)
'''

