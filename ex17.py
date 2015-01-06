# Exercise 17
print "====================== Exercise 17: More Files ======================= "
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#hot to do the below in one line - Later
in_file = open(from_file).read()
#indata  = in_file.read()

print "The input file is %d bytes long" % len(in_file)
print "Does the input file really exists?  %r" % exists(to_file)
print "Does the output file really exsits %r" % exists(from_file)

print "Ready, hit RETURN to continue, CTRl+C to abort.,"
raw_input()

out_file = open(to_file, 'a').write(in_file)
#out_file.write(indata)
#out_file.write(in_file)

print "Alright,  all done. "
#out_file.close()
#in_file.close()

#print "the lenght of the new file is %d" % len(out_file)
print "====================== End of Exercise 18 ============================="
