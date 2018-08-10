from sys import argv

script, filename = argv
file_obj = open(filename)
print(file_obj.read())

new_file = input("> ")
new_file = open(new_file)
print(new_file.read())