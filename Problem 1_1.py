"""
Problem 1.1
"""

# Creating dictionary from Table 1
my_dict = {"0": "zero",
           "10": "ten",
           "20": "twenty",
           "30": "thirty",
           "40": "fourty",
           "50": "fifty",
           "60": "sixty",
           "70": "seventy",
           "80": "eighty",
           "90": "ninety",
           "100": "hundred"}


run_main = True # Defining boolean variable to control while loop

while run_main: # Starting while loop
    try:        # Using try to test valid user input
        # Get and store user input
        user_input = input("Enter the number you want to " +
            "know the English word for (0, 10, 20...100): ")
        dict_value = my_dict[user_input] # Look up input as key in dict
    # Raise error if input is not valid key in dict:
    except KeyError:
        # Print error message
        print("Sorry, the input was not valid.")
    else:  # If valid key in dictionary
        # Print result
        print(f"The English word for {user_input} is {dict_value}")
        run_main = False # Turn off while loop for main program

