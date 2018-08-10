#import argv function from sys module
from sys import argv
# set a postional parameter to input
script, filename = argv
# we took content of a variable {filename} and made
#a file object out of it
txt = open(filename)
print(f"Here's your file {filename}:")
#printed to stdout a content of the file object
#wich is received by read function
# print(txt.read())
# #print a metainfo of the file
var = txt.read()
print(f"One more time lets print a {filename}")
print(txt.readline())

#print(var[1])
#
txt.close()
#print(txt.read())
# print("Type the filena,e again:")
# file_again = input("> ")

# txt_again = open(file_again)
# print(txt_again.read())