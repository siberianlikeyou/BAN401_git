"""
Problem 2
"""

def range_replacement(start, stop):
    """
    This is a recursive function to replace the range() function
    as the problem does not allow the use of this built-in function.

    This takes the "start" parameter which indicates the starting number
    of the range, and the "stop" parameter which indicates what number
    we want to create the list up to (but not including).

    The function returns a list with "stop" number of elements,
    going from "start" until (stop-1) in increments of 1.
    """

    if stop == start:  # Base-case: check if stop is equal to start
        return[]       # If so, reached base-case: stop recursion
    # If number is not 0, return the [stop-1] as list value
    # and recurse (call function again) with (stop-1) as "stop" argument
    return range_replacement(start, stop-1) + [stop-1]


def selectionSort(my_list):
    """
    The selection sort looks for the largest value as it makes a pass,
    and after completing the pass, places it in the proper location.

    Source for SelectionSort code is from:
    https://www.pythoncentral.io/selection-sort-implementation-guide/

    Parameter: new_list, a list to be sorted.
    Returns: Sorted list. Note that this function sorts the list given as
    argument, it does not return a new, sorted list.
    """

    # Start for loop iterating over length of list
    for i in range_replacement(0, len(my_list)):

        # Store current element i as minPosition
        minPosition = i

        # Start for loop iterating over all elements of list after i
        for j in range_replacement(i+1, len(my_list)):
            if my_list[minPosition] > my_list[j]:   # If this element is larger than current element j
                minPosition = j                     # Save current index as new minPosition

        # Swap the found minimum element with minPosition
        temp = my_list[i]                   # Store the to-be-swapped element
        my_list[i] = my_list[minPosition]   # Replace element at minPosition to position i
        my_list[minPosition] = temp         # Put the temporary element in the slot of the minPosition number

    return(my_list) # Return the sorted list


def get_the_chain(numberlist):
    """
    This function takes parameter numbers: a list of integers
    of any length, and returns the longest chain of numbers
    contained within as well as the original list of numbers.
    If there are multiple chains of longest length, returns
    the one with the highest starting value.
    """

    sorted_list = list(numberlist)           # Create a copy of the original list
    sorted_list = selectionSort(sorted_list) # Sort the new list


    maxlength = 0           # Create variable to store longest chain so far
    chain_list = []         # Create empty list to store chains
    active_chain = False    # Create boolean variable to store if currently on chain
    temp_chain = []         # Create empty list to store temporary chain


    for i in range_replacement(0,len(sorted_list)-1):

        # Check if current element is 1 lower than next element in list
        if sorted_list[i] == sorted_list[i+1]-1:
            # Append current value to the nested list of chains
            temp_chain.append(sorted_list[i])
            # Set active_chain to true
            active_chain = True

        # Check if current element is duplicate of next element
        elif sorted_list[i] == sorted_list[i+1]:
            continue # skip and go to next iteration of for loop
        # If next number is not in chain
        else:
            # Check if there is currently an active chain
            if active_chain:
                # Add current number to chain list
                temp_chain.append(sorted_list[i])

                # Check if the current chain is longer than previous longest
                if len(temp_chain) >= maxlength:
                    # Append current chain to list of chains
                    chain_list.append(temp_chain)
                    maxlength = len(temp_chain)


                # Clear temporary chain list
                temp_chain = []
                # Turn off active_chain
                active_chain = False


    # Out of for-loop: Check the last number in list
    # Check if there is currently an active chain
    if active_chain:
        # Add last number number to chain list
        temp_chain.append(sorted_list[-1])
        # Check if the current chain is longer than previous longest
        if len(temp_chain) >= maxlength:
            # Append current chain to list of chains
            chain_list.append(temp_chain)
            maxlength = len(temp_chain)

    return(chain_list[-1]) # Return the longest chain

# Run with test data:
numbers = [0, 7, 4, 8, 1, 3, 8, 10, 11, 2, 5, 12, 9]
# Print original list
print(f"Example numbers: {numbers}")
# Print longest chain returned from get_the_chain function
print(f"Longest chain: {get_the_chain(numbers)}")


