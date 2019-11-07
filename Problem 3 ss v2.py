"""
Problem 3
"""
class Student:
    """
    Student object.
    Arguments:
        Self-explanatory, properties of students given in the problem
        description.
    Returns:
        No returns, but has __str__ for printable representation of
        student information and listView property for printable
        representation to be used in lists with multiple students.
    """
    # Initializing variables to be stored in Student object
    def __init__(self, id, firstName, lastName, GPA, major, groups =[]):

        # Initialize variables
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.GPA = GPA
        self.major = major
        self.groups = groups

    # Using str magic method to create printable representation of object
    def __str__(self):
        # Creating printable version of group membership
        group_print = str()
        # If student is a member of any groups
        if self.groups:
            for group in self.groups:
                # Add group(s) to the print variable
                group_print = group_print + "  - " + group + "\n"
        else: # No group membership
            group_print = "N/A\n"

        # Specify printable return in correct format
        return f"Retrieving data for student {self.firstName} " +\
            f"{self.lastName} (student ID {self.id})\n" + \
            f"- GPA: {self.GPA} \n" + \
            f"- Major: {self.major} \n" +\
            f"- NHHS Group membership: \n{group_print}"

    # Create class method to get printable version of student information
    # to be used in list view with multiple students
    def listView(self):
        return f"{self.firstName} {self.lastName} (ID {self.id})"
# End of class Student

def helper_add(student_list):
    """
    Helper function to enter data into search_dict.
    Param student_list is a supplied list of student objects.
    Has no return, just populates search_dict.
    """

    def add_check(key, value):
        """
        Helper function to check if someone with same name(s) or ID
        already exists, then add it accordingly.
        Key parameter: the student object to add
        Value parameter: the name(or ID) to check if already exists in
        the search_dict.
        Has no return, adds key:value pair if key didn't exist,
        or appends it to list of objects if key already exists (i.e.
        multiple students with same first/last name)
        """
        if value not in search_dict:
            # Add to search_dict as first element of list
            search_dict[value] = [key]
        else:                              # If key already exists
            search_dict[value].append(key) # Append to existing list

    # Adding all search parameters as keys to search_dict using add_check
    for student in student_list:
        add_check(student, student.firstName)
        add_check(student, student.lastName)
        add_check(student, student.firstName + " " + student.lastName)
        add_check(student, student.lastName + " " + student.firstName)
        add_check(student, student.id)

def search_function(user_search):
    """
    Search function to be called from main program.
    Searches the search_dict for student, and if multiple matches
    let's user choose. Function also validates input at every step.
    Param user_search: search string to search search_dict for.
    Returns: Search result as f-string (printable)
    """
    try:
        # Look if search input is in search_dict
        search_result = search_dict[user_search]
    except KeyError:
        return("No matches found.")
    else: # Found a match in search_dict:
        # Check if 1 or multiple matches
        if len(search_result) == 1:
            # If only 1 result, return it:
            return(f"----------------\n"
                   f"One match found. \n" 
                   f"----------------\n" 
                   f"{search_result[0]}")
        # If several results:
        else:
            print(f"Several results matched your query:")
            index = 1 # Create counter to index results
            for id in search_result:
                # Print each result
                print(f"{index}. {id.listView()}")
                index += 1 # Increase counter every loop

            input_control = True # Variable for flow control of while loop
            while input_control:
                user_choice = \
                    (input("Enter the number of the search result for "
                    "which you want to retrieve the info\n or enter" 
                    " 'all' to print info for all matching results\n"))
                # Check if user wants all results
                if user_choice.lower() == "all":
                    print(f"All {len(search_result)} search results: \n"
                          "----------------")
                    for student in search_result: # print all results
                        print(f"{student}"
                              "----------------")
                    input_control = False
                    return("End of results.\n") # end function

                else:
                    try: # Validate that user typed valid index
                        user_choice = int(user_choice) # Check for integer
                        if user_choice < 1:  # Check for positive integer
                            raise ValueError
                        # Positive integer input: check that input is
                        # one of the numbers displayed in the list
                        chosen_student = search_result[user_choice-1]
                    # If positive integer is higher than list
                    except IndexError:
                        print("Incorrect input. Please try again.")
                    # Other invalid inputs (letters, negative numbers)
                    except ValueError:
                        print("Incorrect input. Please try again, with "
                              "a number.")
                    else: # Return chosen result
                        return(f"----------------\n{chosen_student}"
                               f"----------------")
                        input_control = False  # Turn off flow control
            # End of while loop



# Input student list of student objects
student_list = [
    Student("19710", "Mike", "Wheeler", 3.5, "FIE", ["it.gruppen"]),
    Student("19670", "Nancy", "Wheeler", 3.6, "ENE", ["K7 Bulletin", "NHHS Opptur", "NHHS Energi"]),
    Student("19660", "Steve", "Harrington", 2.4, "STR"),
    Student("18119", "Mike", "Wazowski", 2.9, "BAN"),
    Student("69420", "Jeffrey", "Lebowski", 4.2, "BLZ", ["NHHI Bowling", "NHHI Vinum"]),
    Student("12345", "Ivan", "Belik", 1.8, "BAN", ["it.gruppen", "NHHS Consulting"]),
    Student("11007", "Sterling", "Archer", 2.7, "MBM", ["NHHI Lacrosse"])
]

search_dict = dict()     # Create empty search dictionary
helper_add(student_list) # Populate search dictionary

# Start of main program
run_program = True # Flow control variable for main program loop
while run_program:
    user_search = input("Who are you looking for?\n").title()
    print(search_function(user_search)) # Call search function
    # Inner while loop to validate input after search is done
    while run_program:
        search_again = input("Would you like to make a new search? (y/n)\n")
        if search_again.lower() == "y":
            break # return to outer loop for new search
        elif search_again.lower() == "n":
            print("Exiting the program...")
            run_program = False # Turn of flow control to end program
        else: # Any other input than "y" or "n"
            print("----------------\n"+
                  "Incorrect input. Please try again.\n"+
                  "----------------")

