# Exercise  33: While Loop
print "================ Exercise 33: While Loop  ======================"

i = 0
numbers = []

'''
while i < 6:
        print '\n'
        print "At the top i is %d" % i
        numbers.append(i)
        i = i+1
        print "Numbers now:", numbers
        print "At the botton i is %d" % i
print '\n'
print "The numbers:"
for num in numbers:
        print num
'''

print '\n'

def print_numbers(test, i, numbers):
        #i = 0
        #numbers = []
        while  i < test :
                print '\n'
                print "Using Function call : At the top i is %d" % i
                numbers.append(i)
                i = i + 1
                print "Numbers now:", numbers
                print "At the botton i is %d" %i
        print '\n'
        #print "The Numbers:"
        #for num in numbers:
        #       print num
        return numbers


#Declaration
i = 0
test = 100
numbers = []
num = print_numbers(test, i, numbers)
print "The numbers are", num

for letter in 'BasharaWani':
        print "Current Letter:", letter

print "================ End of the Exercise 33: While Loop  ============"
                                                                                           