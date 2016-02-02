from sys import argv
#takes the arguments and the script plays out. 
#one of the arguments is always going to be the filename
#script,filename = argv
script = argv
#this is basically to call the file into text and open the contents
#txt = open(filename)

#print "Here is your file %r" %filename
#print txt.read()
#read the contents, just like applying a function 
#to the file
#taking the name of the file as input
print "Type the filename  : "
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()


