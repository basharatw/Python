from sys import argv

script, filename= argv

print "We'r going to erase %r." % filename
print "If you do not want that hit CTRL-C (^C)."
print "If you want do that, hit RETURN"
raw_input("?")
print "Opening the file...."
target = open(filename,'a')

#print "Truncating the file name. Goodbye!!!!! "
#target.truncate()

print "Now I will be asking you for three lines"
line1 = raw_input("Line 1:")
line2 = raw_input("Line 2:")
line3 = raw_input("Line 3:")

print "I am going to write these to a file."
lines = (line1, line2, line3)
target.write('\n'.join(lines))
target.write("\n")

print "Finally we will close the file...."
target.close()

