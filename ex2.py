#Now this is second file
#python ex2.py Tom Python
print "======================== Exercise 14: Promoting and Passing =========="


#from sys import argv
#script, first, second=  argv
#print "This script is called:", script
#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third

from sys import argv

script, user_name, programming = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."

print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "You like %s programming language, Nice!!!! " %programming

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
You have a %r computer and you like %s.  Nice.
""" % (likes, lives, computer, programming)
print "========================== End of exercise 14 ===================="

print "============================= Exercise 15 : Reading Files ==========="
print "============================= End of exercise 15 ==================="
