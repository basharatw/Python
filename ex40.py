#Exercise 40: Modules, Classes, and Objects
import mystuff

print "=============== Start of Exercise 40 : Modules, Classes and Objects ======================"
#mystuff={'apple': "I AM APPLES!"}
#print mystuff['apple']
#mystuff.apple()
#print mystuff.tangerine

# Let us buidl first a Class
class Song(object):
   def __init__(self, lyrics):
      self.lyrics = lyrics

   def sing_me_a_song(self):
        print '========================='
        for line in self.lyrics:
                print line

# Let us build a class
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary, age, state, country):
      self.name = name
      self.salary = salary
      self.age = age
      self.state = state
      self.country = country
      Employee.empCount += 1

   def displayCount(self):
      print "Total Employee : %d" % Employee.empCount

   def displayEmployee(self):
      print  ("Name :   "), self.name
      print  ("Salary : "), self.salary
      print  ("Age :    "), self.age
      print  ("State :  "), self.state
      print  ("Country :"), self.country
      print  ("\n")


# Let us build another class
class BankAccount:
   'Bank account for the all employees'

   def __init__(self):
      self.balance = 0

   def withdraw(self, amount):
        self.balance = self.balance - amount
        print "Balance after withdraw", self.balance
        return self.balance

   def deposit (self, amount):
        self.balance = self.balance + amount
        print "Balance after deposit", self.balance
        return self.balance

# Initialize the classes
bankAcc1  = BankAccount()
bankAcc2  = BankAccount()

# Now call the methods inside the classes
dep1 = bankAcc1.deposit(100)
dep2 = bankAcc2.deposit(50)
print dep1
print dep2

withd1 = bankAcc1.withdraw(10)
withd2 = bankAcc2.withdraw(10)

print withd1
print withd2



'''
# ================== Using the classes and Data population ============================
# Class = Employee
emp1 = Employee("Sam1", 2000,20,"NY", "USA")
emp1.displayEmployee()
emp2 = Employee("Sam2", 2000,20,"NY", "USA")
emp2.displayEmployee()
emp3 = Employee("Sam3", 2000,20,"NY", "USA")
emp3.displayEmployee()
emp4 = Employee("Sam4", 2000,20,"NY", "USA")
emp4.displayEmployee()
emp5 = Employee("Sam5", 2000,20,"NY", "USA")
emp5.displayEmployee()
emp6 = Employee("Sam6", 2000,20,"NY", "USA")
emp6.displayEmployee()
emp7 = Employee("Manni", 2000,20,"NY", "USA")
emp7.displayEmployee()
emp1.displayCount()
#print ("Total Employee %d") % Employee.empCount
#print ("Total Employee %d") % Employee.empCount

# Class =  Song
songLyrics = ["Happy birthday to you",
              "I don't want to get sued",
              "So I'll stop right there"]
song1 = Song(songLyrics)
print '\n'
song1.sing_me_a_song()

songLyrics2 = ["They rally around tha family",
               "With pockets full of shells"]
song2 = Song(songLyrics2)
print '\n'
song2.sing_me_a_song()
'''

print "=============== End of Exercise 40 : Modules, Classes and Objects ======================"
                                                                                                     


