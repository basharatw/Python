# Working with Lists
print "=============== Start Exercise 38:Doing Things to Lists =============="

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
print "Stuff= %s " % len(stuff)
print "More Stuff= %s " % len(more_stuff)
print '\n'

while len(stuff) != 10:  #We will only care for 10 items
    next_one = more_stuff.pop() # get the last one
    print "Stuff= %s " % len(stuff)
    print "Adding: ", next_one # print it
    stuff.append(next_one) # add it to the stuff list
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff
print "Let's do some things with stuff."

print stuff[0]
print stuff[1]   #first element
print stuff[-1] # whoa! fancy Last element
print stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar!

print "=============== End of Exercise 38:Doing Things to Lists ============="
