# Python-Classes-and-Inheritance
.method() => it's a method called upon an object; function() => it's a function which takes arguments as inputs.

#### If you think of a class as kind of a factory, instances are the things that the factory produces.

An instance variable is a variable that kind of lives inside of an instance. So if point1.x = 5, and point2.x = 10, then these are setting instance variables called x for point1 and point2.

#### A method is like a function except it belongs to a class. One difference between methods and functions, is that methods always have at least one argument.

#### A constructor is a special method that's meant to initialize instances, including instance variables.

#### __init__ (underscore underscore in it underscore underscore / dunderscore in it dunderscore) is the python constructor. Mind it!!!

When Python evaluates any instance variable or a class variable, it first looks inside of the instance and then it looks inside of the class. If it doesn't find the desired method inside of the instance or inside of the class, then it's going to throw a runtime error.

#### toString method in python is __init__(self). Mind it!!!

#### __init__(self) is a like a built-in constructor in python class which defines how the class instance / object would be represented when it's called. It actually provides the `print() format` of the class instance.

#### So, when you create a class, you often want to set the __str__(self) method in order to get more readable and understandable things to print out when you actually print out any particular instance. 

#### __add / sub / multiply/ divide__(self) is a way of overwriting built-in methods. __something__() overwrites the built-in methods.

#### Mind it, mentioning `self` inside a function or method definition implies that `self` is not an argument. That's the instance of the class upon which the method can be called as `instance of class (as self).method()`. That's it!!! Again mind it, `self` is just a keyword to represent the instance of the class upon which the method can be called.

We have instance variables that belong to every particular instance and we have class variables which belong to a class.


















































