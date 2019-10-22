import <module>
from <module> import *
from <module> import <something>

if <statement>:
    <do something>
elif <statement>:
    <do something>
else:
    <do something>
for i in range(<_from>, <to>, <step>):
    <do something>
    break
    continue
while <statement>:
    <do something>
    break
    continue
def a_function_name (*args):
    #note exactly 4 lines intended with the whitespace
    <some stuff>
def a_function_name (arg1, arg2, etc):
    <some stuff>
    global i #declares that used i is from a global scope

def divide(dividend, divisor):
    try:
        return dividend/divisor
    except:
        print('Error: Invalid argument')

#Reserved words: True, False, None
a = None #equivalent to Null, class NoneType

#list value with two lists inside
someList = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(someList[0]) # will return list ['cat', 'bat']
print(someList[0][0]) # will return string 'bat' (or int if you would refer to any of someList[1][...] value)
# same apply for even deeper nested lists
integerList = someList[1][0:2] #that integers with the colon is called "a slice", returns range of indexed values
i = len(someList) #will return 2 cause of there are 2 items inside someList list

i_list = ['dog', 'cat']
added_list = someList + i_list
multiplied_list = i_list * 2 # will create ['dog', 'cat', 'dog', 'cat'] list

y_list = []
y_list += [<object>] #update list with a new value
del i_list[1] #deletes 'cat' from i_list 
del i #removes previously declared variable

for i in someList:
    <itrates over a list>

#multiple assignment
cat = ['fat', 'black', 'loud']
size, color, disposition = cat

#assiging y a reference to the list cat
y = cat #changes in list y will change original list cat
#creates a new list, copy of the original: (requires copy module)
z = copy.copy(cat)
z = copy.deepcopy(someList) #for lists inside

# LIST METHODS
#finding a value in the list with .index() method
a = cat.index('fat') #will return 0
a = cat.index('big') #will return a ValueEror
#add a value to a list (with the use of list methods)
cat.append('angry')
cat.insert(<where (index)>, <what (object)>)
#remove a value to a list (with the use of list methods)
cat.remove('angry')
#sorting (do not apply to a complex list with both int and str)
cat.sort() # uses ASCII-betical order
cat.sort(reverse=True) 
cat.sort(key=str.lower) #regular alphabetical order

# work with string as with a list
name = 'Zophie'
name[0]
#'Z'
name[-2]
#'i'
name[0:4]
#'Zoph'
'Zo' in name
#True
'z' in name
#False
'p' not in name
#False
for i in name:
    print('* * * ' + i + ' * * *')

#Tuples (immutable lists)
new_tuple = ('one', 'two', 'three', 23, 0.1)
single_item_tuple = ('one',)

# converting lists and tuples
list(_tuple)
tuple(_list)

#The Dictionary Data Type
myCat = {'size'      : 'fat',
        'color'      : 'gray',
        'disposition': 'loud'
        12345           : 'numbers as key'} # only zero can't be a key to a dict value
a = myCat['color'] #assign gray str value to "a" variable
myCat['behave'] = 'good' #added a key:value pair "behave:good" to the dict

if <key_to_try> in myCat: #will retur True if the value <key_to_try> exists as a key in the dictionary myCat
a = myCat.keys()
a = myCat.values()
a = myCat.items()

#for with multiple values at a time
spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('Key: ' + str(k) + ' Value: ' + str(v))
a = spam.get(<key_in_spam>, <default_value>) # the <default_value> (fallback value) will be returned if there no <key_in_spam> key found in the spam dict
spam.setdefault('color', 'black') #will add color:black if there no "color" key present
pprint.pprint(<to_print>)
a = pprint.pformat(<to_print>) #return pretty format intp string

#working with strings
s = 'Hello'
s =  s.upper()
s =  s.lower()
s =  s.islower() #true
s =  s.isupper() #false
s =  s.isalpha()
s =  s.isalnum() #nubers and letters
s =  s.isdecimal() #only numbers and no spaces
s =  s.isspace() #only space character (space, tabs, new lines)
s =  s.istitle() #returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.
s =  s.startswith(<string>)
s =  s.endwith(<string>)

_str = ', '.join(['cats', 'rats', 'bats'])
# _str == 'cats, rats, bats'
_list = _str.split(<split char>) # for <split char> space is a default, but can be a \n or something else
#_list == ['cats', 'rats', 'bats']
_str.strip(<string>) #remove multiple <string>s from both sides
_str.rstrip(<string>)
_str.lstrip(<string>)

#REGULAR EXPRESSIONS
import re
_compile_objext = re.compile(<regex to match>)
_match_object = _compile_object.search(<text to search>) #will return only first match
_sting = _match_object.group(<group_index_int>) 
_list = _compile_object.findall(<text to search>) #will return all matches
_new_compile_objext = re.compile('.*', re.DOTALL) # dot as a wildcard for a newline as well