from sys import argv

script , filename = argv

print "We're going to erase %r" %filename
print "If you don't want to do that hit CTRL-C"
print "If you want to do that , hit return"

raw_input("?")

print "Opening the file..."
target= open(filename, 'w')