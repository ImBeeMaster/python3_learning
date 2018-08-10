from sys import argv
from os.path import exists
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")
in_file = open(from_file)
# indata = in_file.read()
out_file = open(to_file, 'r+')
out_file.write(in_file.read())

# print(f"The input file is {len(indata)} bytes long")
# print(f"The input file is {len(in_file)} bytes long")
print(f"Does the output file exists? {exists(to_file)}")
input()

# out_file = open(to_file, 'r+')
# out_file.write(in_file.read())
print("Alright all done.")

out_file.close()
out_file = open(out_file.name)
print(out_file.read())
out_file.close()
in_file.close()