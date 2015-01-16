# Exercise  32: Loop and Lists and Multi Deimestional Lists
print "================ Exercise 32: Loop and Lists  ======================"

#List are like arrays
the_count = [1,2,3,4,5,6,7,8,9,10]
fruits    = ['apples', 'oranges','banana', 'grapes','pears', 'apricots']
change    = [1, 'pennies', 2,'dimes',3,'quarters']
print '\n'

# this first kind of for-loop goes through a list
for number in the_count:
        print "This is count %d" % number

print '\n'

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

print '\n'
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

print '\n'
# We can also build lists, first start with  empty one
elements = []

elements = range(0,15)
print "Test Range for the elements : %s " % elements

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

print '\n'
# Now we can print them out too
for i in elements:
        print "Element was: %d" % i

print '\n'
print "============= Start of Multi Dimesional Arrays Lesson ==============="
a = [0, 1, 3, 9, 8, 7] #create a list and append it
a.append(3)
a.append(5)
a.append(11)
print a
a.sort()
print a
a.reverse()
print a

print '\n'
array =[[0,1,2],[3,4,5],[6,7,8]]
print array[0]
print array[2]
print array[1]
print '\n'

#a = zeros(5)
#a[1,2] = 8
#print a


print "============= End of Multi Dimesional Arrays Lesson   ==============="





print '\n'
print "================ End of the Exercise 32: Loop and Lists  ======================"
                                          
