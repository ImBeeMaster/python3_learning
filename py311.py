from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-c (^C).")
print("If you do want this, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncationg the file. Goodbye!")
target.truncate()
print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

target.write(f"{line1}\n{line2}\n{line3}\n")
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
target.close()