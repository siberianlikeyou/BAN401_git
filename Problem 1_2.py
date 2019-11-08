"""
Problem 1.2
"""

# Get input sequence and split input. Convert this into set,
# then convert to list and sort this list.
# Finally, print list.
print(" ".join(sorted(list(set(input(
    "Enter your sequence of words: \n").split())))))


