"""
Problem 2
"""

numbers = [45, 56, 8, 92, 43, 5, 6, 44]



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
    for i in range(len(my_list)):

        # Store current element i as minPosition
        minPosition = i

        # Start for loop iterating over all elements of list after i
        for j in range(i+1, len(my_list)):
            if my_list[minPosition] > my_list[j]:   # If this element is larger than current element j
                minPosition = j                 # Save current index as new minPosition

        # Swap the found minimum element with minPosition
        temp = my_list[i]                 # Store the to-be-swapped element
        my_list[i] = my_list[minPosition]   # Replace element at minPosition to position i
        my_list[minPosition] = temp       # Put the temporary element in the slot of the minPosition number

    return(my_list) # Return the sorted list



print(selectionSort(numbers))