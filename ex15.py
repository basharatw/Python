#Example of reading from a file

print "============= Exercise 15 : Reading from a file =============="
from sys import argv

#define the invidual arguments i.e the script file name "ex15.py" and filename = ex15_sample.txt
script, filename = argv

#open the file
txt = open(filename)

#print the file name
print "Here's your file %r:" % filename
#now read from the open file and print
print txt.read()
txt.close()
print "=================  End of the exercise 15 ===================="

