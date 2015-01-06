#Function and Variables
def cheese_and_crackers(cheese_count, boxes_of_chocolate):
        print "You have %d cheese!" % cheese_count
        print "You have %d boxes of crackers!" % boxes_of_chocolate
        print "Man that's enough for a party!"
        print "Get a blanket. \n"
        print "This is end of function creation. \n"

print "We can just give the fucntion numbers directly"
cheese_and_crackers(20,30)
cheese_and_crackers(100,200)

print "Or, we can use varaibles from our scripts:"
cheese_count = 123
boxes_of_chocolate= 321
cheese_and_crackers(cheese_count, boxes_of_chocolate)

print "We can do math inside too:"
cheese_and_crackers(10+20+30,100-1 )

print "And we can combine the two, variables and math"
cheese_and_crackers(cheese_count+1000 , boxes_of_chocolate*999)

