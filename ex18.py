#This one is like scripts with argv
def print_two(*args):
        arg1, arg2 = args
        print "arg1: %r, arg2: %r" % (arg1, arg2)


#* args is pointless, we can do the below
def print_two_again(arg1,arg2):
        print "arg1: %r, arg2: %r " % (arg1, arg2)

#This taked one argument
def print_one(arg1):
        print "arg1: %r" %(arg1)

#This takes no arguments
def print_none():
        print "I got nothing."

#Call the above functions now
print_two("Zed", "Shaw")
print_two_again("Basharat", "Wani")
print_one("Basharat")
print_none()


