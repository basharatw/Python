
# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.

print "I could have code like this."
# and the comment after is ignored
# You can also use a comment to "disable" or comment out a piece of code:
# print "This won't run."

print "This will run."
#Test Program
print "Hello Again"
print "I like typing this."
print "This is fun."
print 'Yay! Printing.'
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'
print "Basharat is writing Python code."
print "Now Day II "

print "================== Number and Maths ========================"
#Number and Maths Section

print "I will now count my chickens:"
print "Total Hens are 30, Answers is   = ", 25 + 30 / 6
print "Roosters 25%, Answer is ",  100 - 25 * 3 % 4
print "Now I will count the eggs:"

#print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"
print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7
print "Oh, that's why it's False."
print "How about some more."
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

print "==================End Numbers and maths ===================="
#End of Maths and Operations
#Variables and Names
print "=================== Variables and Names ===================="
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = space_in_a_car * cars_driven
average_passengers_per_car = passengers / cars_driven
print "Cars Not Driven                  = "  ,  cars_not_driven
print "Total Drivers                    = "  ,  cars_driven
print "Carpool Capacity                 = "  ,  carpool_capacity
print "Average Passengers per car       = "  ,  average_passengers_per_car
print "=================== End Variables and Names ================="
#End Variables and names

print ""
print "======================= Chapter 5 : Variable and Strings =============="
#String Decl
myName   = 'Basharat Wani'
myEyes   = 'Brown'
myTeeths = 'White'
myHair   = 'Black'

#Decimal and Number Declaration
myAge    = 40   #age
myHeight = 170 #height in cm
myWeight = 138 #wieght in pound

print "Let's us talk about this %s" % myName
print "He's %d inches tall.       " % myHeight
print "He's %d pounds heavy.      " % myWeight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair"% (myEyes,myHair)
print "His teeth are usually %s depending on the coffee." % myTeeths
print "If I add %d, %d, and %d I get %d."                                                     %(myAge, myHeight, myWeight, myAge + myHeight + myWeight )
print ""
x= "Example of using Str and Repr function--- "
print "Printing STR function example =  %s" %x
print "Printing REPR function exampe =  %r" %x
print ""

left  = "This is the left side"
right = "this si the right side"
print left + right

print "======================= End of Chapter 5 ============================="

print "====================== Start of Chapter = 6 =========================="
x       = "There are %d types of  People " %10
binary = "Binary"
do_not = "don't"
y       = "Those who know %s and those who %s." % (binary,do_not)

print x
print y

#Remember using r this will return exactly the string
print "I said: %r" % x
print "I also said: '%s'." %y
hilarious = False
joke_evaluation = "Is't that Joke so funny! %r"
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
print 'Py' 'thon'
print "====================== End of Chapter 6 =============================="

print "====================== Start of Chapter 7 More Printing =============="
print "Mary has a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went"
print "." * 10

end1= "C"
end2= "h"
end3= "e"
end4= "e"
end5= "s"
end6= "e"
end7= "B"
end8= "u"
end9= "r"
end10= "ger"

#watch this commetns now
print end1+ end2 +end3 +end4 +end5 +end6,
print end7 +end8 +end9 +end10

print "====================== End of Chapter 7                 =============="

print "===================== Exercise 8: Printing, Printing    =============="
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

days   = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMarch\nApril\nMay\nJune\nJuly\nAugust\nSeptember\nOctober\nNovember\nDecember"

print "Here are the days of the week:", days
print "Here atre the months of the year:", months

tabby_cat = "\tI'm tabbed in."
persian_cat ="I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat ="""
I'll do a list:
\t* Cat Food
\t\t\t\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "I am 6'2\" tall."
print 'I am 6\'2" tall.'

#while True:
#    for i in ["/","-","|","\\","|"]:
#        print "%s\r" % i,

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, your are %r old., %r tall, %r heavy. " % (age, height, weight)

print "Now using Name promts without print function"
age = raw_input("How old are you? ")
height = raw_input("How tall are you?" )
weight = raw_input("How much do you weight?")
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
pydoc raw_input()

print "===================== End of Exercise 8                 =============="


