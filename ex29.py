#Exercise 29: What If
print "============== Start Exercise 29: what If ======================="

people  = 20
cats    = 30
dogs    = 15

print people, cats, dogs
print "\n"

if people < cats:
        print "Too many cats! The world is doomed!"

if people > cats:
        print "Not many cats! The world is saved!"
else:
        print "Less number of people %s then cats %s !" % (people, cats)

if people < dogs:
        print "The world is drooled on!"
else:
        print "Less number of dogs then people."

if people > dogs:
    print "The world is dry!"

dogs += 5
print "Number of Dogs got incremented to %s" % dogs

if people >= dogs:
        print "People are greater than or equal to dogs."

if people <= dogs:
        print "People are less than or equal to dogs."

if people == dogs:
        print "People are dogs."
print "\n"

print "============== End Exercise 29: what If   ======================="


