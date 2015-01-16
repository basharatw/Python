# Let is build a class

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
      print ("Total Employee :", Employee.empCount)

   def displayEmployee(self):
      #print ("Name : ", self.name,  ", Salary: ", self.salary)
      print  ("Name : ", self.name)
      print  ("Salary : ", self.salary)
      print  ("Age : ", self.age)
      print  ("State : ", self.state)
      print  ("Country : ", self.country)
      print  ("\n")

"This would create first object of Employee class"
emp1 = Employee("Sam1", 2000,20,"NY", "USA")
emp2 = Employee("Sam2", 2000,20,"NY", "USA")
emp3 = Employee("Sam3", 2000,20,"NY", "USA")
emp4 = Employee("Sam4", 2000,20,"NY", "USA")
emp5 = Employee("Sam5", 2000,20,"NY", "USA")
emp6 = Employee("Sam6", 2000,20,"NY", "USA")
emp7 = Employee("Manni", 2000,20,"NY", "USA")

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp4.displayEmployee()
emp5.displayEmployee()
emp6.displayEmployee()

emp1.displayCount()

#print ("Total Employee %d") % Employee.empCount
#print ("Total Employee %d") % Employee.empCount



