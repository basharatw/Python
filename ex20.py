#Exercise 20: Functions and files
from sys import argv

script, input_file = argv

def print_all(f):
        print f.read()

def rewind(f):
        f.seek(0)

def print_a_line(line_count,f ):
        print "======================"
        print line_count, f.readline()
        print "======================"

current_file = open(input_file)

print "First let's print the whole file :\n"
print_all(current_file)
print "Now let's rewind, kind of like a tape."
rewind(current_file)


print "Let's print the next five lines:"
# Now let us the function
current_line = 1
print "Current Line : %d" %current_line
print_a_line(current_line,current_file)

#this will increment the varaiable by 1
current_line += current_line
print "Current Line using +1 =  %d" %current_line
print_a_line(current_line, current_file)

current_line = current_line  +1
print "Current Line : %d" %current_line
print_a_line(current_line, current_file)

current_line = current_line +1
print "Current Line : %d" %current_line
print_a_line(current_line, current_file)

print "Current Line : %d" %(current_line+1)
print_a_line(current_line+1, current_file)

#How to use enumerate function
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
print "Seasons %s"  %list(enumerate(seasons, start=1))
print "Let's print the next five lines:"

print "Function and Files \n"
                                          
