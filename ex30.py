#Exercise 30: What If Else and If
print "============== Start Exercise 30: What If Else and If ======================="

people  = 20
cars    = 30
trucks  = 15

print "People: %s, Cars: %s and Trucks are %s  " %(people, cars, trucks)
print "\n"

if  cars > people:
        print "We should take the cars."
elif cars < people:
        print "We should not take the cars"
else:
        print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
        print "Alright, let's just take the trucks."
else:
        print "Fine, Let's us stay home then"

print "\n"

print "============== End Exercise 30 : What If Else and If  ======================="


