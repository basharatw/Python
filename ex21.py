#Functions can return something
import math
print "========== Exercise 21: Functions can return something ========== "

def add(a, b):
        print "ADDING %d + %d" % (a, b)
        return a + b

def sub(a, b):
        print "SUBTRACTION %d - %d" % (a, b)
        return a - b

def multi(a, b):
        print "MULTIPLICATION %d * %d" % (a, b)
        return a * b

def div(a, b):
        print "DIVISION %d / %d" % (a, b)
        return a /  b

def factorial (a):
        print "FACTORIAL %d " % (a)
        return math.factorial(a)

print "let us do some math with just functions: \n"
a = 20
b = 10

what = add(a,b)
print "This is the return value of the funtion for Addition :%s \n"   % what

what = sub(a,b)
print "This is the return value of the funtion for Subtraction :%s \n" % what

what = multi(a,b)
print "This is the return value of the funtion for Multiplication :%s \n" % what

what = div(a,b)
print "This is the return value of the funtion for Division :%s \n"    % what

a = 4
what = factorial(a)
print "This is the return value of the funtion for Factorial : %s : \n" % what

print "========================="
age = add(30,5) #Addition
height = sub(78,4) #Subtraction
weight = multi(90,2) #Multi
iq     = div(100,2) #Divide
print "========================="

print "Age: %d, Height: %d, Weight: %s, IQ: %s" %(age, height, weight, iq)
print"\n"
print "Here is a puzzle."
what= add(age, sub(height, multi(weight, div(iq, 2))))
print"\n"
print "That becomes: ", what, "Can you do it by hand? \n"

print "========== End of Exercise 21  ========== "

