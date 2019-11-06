"""
Problem 2
"""


def selectionSort(my_list):
    """
    The selection sort looks for the largest value as it makes a pass,
    and after completing the pass, places it in the proper location.

    Main source for SelectionSort code is from:
    https://www.pythoncentral.io/selection-sort-implementation-guide/

    Parameter: new_list, a list to be sorted.
    Returns: Sorted list. Note that this function sorts the list given as
    argument, it does not return a new, sorted list.
    """

    # Creating outer flow control variable for outer while loop
    outer_flow_control = 0
    # Starting while loop
    while outer_flow_control < len(my_list):

        # Store current element i as minPosition
        minPosition = outer_flow_control


        # Create flow control for inner while loop
        inner_flow_control = outer_flow_control+1
        # Start inner while loop iterating over all elements of list after current element
        # of outer while loop
        while inner_flow_control < len(my_list):
            # Check if minPos element is larger than current element in inner loop
            if my_list[minPosition] > my_list[inner_flow_control]:
                # Save current index as new minPosition
                minPosition = inner_flow_control
            inner_flow_control += 1 # Increase inner flow control to continue loop
        # After inner loop is done:
        # Swap the found minimum element with minPosition:
        # Store the to-be-swapped element
        temp = my_list[outer_flow_control]
        # Replace element at minPosition to position of outer loop
        my_list[outer_flow_control] = my_list[minPosition]
        # Put the temporary element in the slot of the minPosition number
        my_list[minPosition] = temp

        outer_flow_control += 1 # Increase outer flow control to continue loop

    return(my_list) # Return the sorted list




def get_the_chain(numberlist):
    """
    This function takes parameter numbers: a list of integers
    of any length, and returns the longest chain of numbers
    contained within as well as the original list of numbers.
    If there are multiple chains of longest length, returns
    the one with the highest starting value.
    """


    def end_chain(maxlength):

        if active_chain:
            print("Ja aktiv")
            # Add last number number to chain list
            temp_chain.append(sorted_list[-1])
            # Check if the current chain is longer than previous longest
            if len(temp_chain) >= maxlength:
                # Append current chain to list of chains
                chain_list.append(temp_chain)
                maxlength = len(temp_chain)

    # END OF FUNCTION
    maxlength = 0  # Create variable to store longest chain so far
    sorted_list = list(numberlist)           # Create a copy of the original list
    sorted_list = selectionSort(sorted_list) # Sort the new list



    chain_list = []         # Create empty list to store chains
    active_chain = False    # Create boolean variable to store if currently on chain
    temp_chain = []         # Create empty list to store temporary chain

    i = 0        # Create flow control variable
    while i < len(sorted_list)-1:

        # Check if current element is 1 lower than next element in list
        if sorted_list[i] == sorted_list[i+1]-1:
            # Append current value to the nested list of chains
            temp_chain.append(sorted_list[i])
            # Set active_chain to true
            active_chain = True

        # Check if current element is duplicate of next element
        elif sorted_list[i] == sorted_list[i+1]:
            i +=1    # increase flow control
            continue # skip and go to next iteration of while loop

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

        i += 1 # increase flow control

    # Out of while loop: Check the last number in list
    # Check if there is currently an active chain
 #   if active_chain:
 #       # Add last number number to chain list
 #       temp_chain.append(sorted_list[-1])
 #       # Check if the current chain is longer than previous longest
 #       if len(temp_chain) >= maxlength:
 #           # Append current chain to list of chains
 #           chain_list.append(temp_chain)
 #           maxlength = len(temp_chain)

    end_chain(maxlength)

    return(chain_list[-1]) # Return the longest chain



# Run with test data:
#numbers = [0, 7, 4, 8, 1, 3, 8, 10, 11, 2, 5, 12, 9]
numbers = [0, 7, 4, 8, 1, 3, 8, 10, 11, 2, 5, 12, 9, 88,89,90,91,92,93,94, 20,21,22,23,24,25,26,27,28]
# Print original list
print(f"Example numbers: {numbers}")
# Print longest chain returned from get_the_chain function
print(f"Longest chain: {get_the_chain(numbers)}")




def outside():
    test_var = True
    outsideList = [1, 2]
    def nested():
        if test_var == True:
            print("Ja")
        outsideList.append(3)
    nested()
    print(outsideList)

outside()

