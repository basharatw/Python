#Animal is-a object (yes, sort of confusing) look at the extra credit
# OO Concepts
# ex42.py

print "======================== Exercise 42: Is-A, Has-A, Objects, and Classes  ====================="

# Base Class Animal
class Animal(object):
    pass

## Is-A
class Dog(Animal):

    def __init__(self, name):
        ## Assign name value
        self.name = name
        print self.name

## Is-A
class Cat(Animal):

    def __init__(self, name):
        ## Assign name value
        self.name = name
        print self.name

# Base Class Person
class Person(object):

    def __init__(self, name):
        ## Assign name value
        ## Person has-a pet of some kind
        self.pet = name
        print self.pet


## Is-A
class Employee(Person):

    def __init__(self, name, salary):
        ## Has A ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary
        print self.salary

## Class Fish
class Fish(object):
    pass

## Is-A
class Salmon(Fish):
    pass

## Is-A
class Halibut(Fish):
    pass

######## Data

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan

## frank has-a salary
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover

## Call Fish
## Call Fish
flipper = Fish()

## Call Salmon
crouse = Salmon()

## ??
harry = Halibut()

print "======================== End of Exercise 42: Is-A, Has-A, Objects, and Classes  ====================="
                    
