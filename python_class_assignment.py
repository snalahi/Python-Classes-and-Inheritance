# Define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively to two instance variables, color and price.
# Assign to the variable testOne an instance of Bike whose color is blue and whose price is 89.99. Assign to the variable testTwo an instance of Bike whose
# color is purple and whose price is 25.0.

class Bike:
    
    # Constructor
    def __init__(self, color, price):
        self.check(color, price)
        self.color = color
        self.price = price
    
    # Argument check
    def check(self, color, price):
        if type(color) != str or type(price) != float:
            raise Exception('color should be string and price should be float')
    
testOne = Bike('blue', 89.99)
testTwo = Bike('purple', 25.0)

# Create a class called AppleBasket whose constructor accepts two inputs: a string representing a color, and a number representing a quantity of apples.
# The constructor should initialize two instance variables: apple_color and apple_quantity. Write a class method called increase that increases the quantity
# by 1 each time it is invoked. You should also write a __str__ method for this class that returns a string of the format: "A basket of [quantity goes here]
# [color goes here] apples." e.g. "A basket of 4 red apples." or "A basket of 50 blue apples." (Writing some test code that creates instances and assigns
# values to variables may help you solve this problem!)

class AppleBasket:
    def __init__(self, color, quantity):
        self.check(color, quantity)
        self.apple_color = color
        self.apple_quantity = quantity
        
    def increase(self):
        self.apple_quantity += 1
    
    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity, self.apple_color)
    
    # Argument check
    def check(self, color, quantity):
        if type(color) != str or type(quantity) != int:
            raise Exception('color should be string and quantity should be integer')
            
# Define a class called BankAccount that accepts the name you want associated with your bank account in a string, and an integer that represents the amount
# of money in the account. The constructor should initialize two instance variables from those inputs: name and amt. Add a string method so that when you
# print an instance of BankAccount, you see "Your account, [name goes here], has [start_amt goes here] dollars." Create an instance of this class with
# "Bob" as the name and 100 as the amount. Save this to the variable t1.

class BankAccount:
    
    def __init__(self, name, amount):
        self.check(name, amount)
        self.name = name
        self.amt = amount
        
    def __str__(self):
        return "Your account, {}, has {} dollars.".format(self.name, self.amt)
        
    # Argument check
    def check(self, name, amount):
        if type(name) != str or type(amount) != int:
            raise Exception('name should be string and amount should be integer')

t1 = BankAccount("Bob", 100)
