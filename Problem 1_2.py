"""
Problem 1.2
"""

testString = "Write Python Code    a sequence word each  word can be Separated another word  Number   of white spaces    a write"


# Alternativ 1
#user_input = input("Enter your sequence of words USERINPUT: ")
#user_input = user_input.split()
#user_input = set(user_input)
#user_input = list(user_input)
#user_input.sort()

#print(user_input)
#print(" ".join(user_input))

# Get input sequence and split input. Convert this into set,
# then convert to list and sort this list.
# Finally, print list.
print(" ".join(sorted(list(set(input(
    "Enter your sequence of words: \n").split())))))


