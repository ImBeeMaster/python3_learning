## Comments here aren't from the book but my understanding of what
##is going on

#set a integer variable for a joke string
types_of_people = 10
#set a string variable for a joke with the previously nnounced variable
x = f"There are {types_of_people} types of people."

#set string variable for a joke
binary = "Binary"
#set another string variable for a joke
do_not = "don't"
#put them to the second joke string
y = f"Those who know {binary} and those who {do_not}."

#display the first joke string
print(x)
#display the second joke string
print(y)

#Lets repeat what we've said
print(f"I said: {x}")
#same here
print(f"I also said: '{y}'")

#set a boolean variable for evaluation
hilarious = False
#set an opposite variable for doubt
doubt = not hilarious
#variable with positional parameters to be passed during invocation
joke_evaluation = "Isn't that joke so funny!? {} and {} at the same time."
#print-function which invoke variable which have to use .format(pos-par-1, ..., pos-par-N) ?method?
print(joke_evaluation.format(hilarious, doubt))

#variable to show us a variable concatenation
w = "This is the left side of..."
#second variable to show us a variable concatenation
e = "a string with a right side."

#the concatenation itself
print(w + e)
