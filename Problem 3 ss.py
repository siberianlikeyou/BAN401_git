"""
Problem 3
"""
class Student:
    """
    DEFINE THIS
    """

    def __init__(self, id, firstName, lastName, GPA, major, groups =[]):

        # Initialize variables
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.GPA = GPA
        self.major = major
        self.groups = groups

    # Using str magic method to create printable representation of Student
    def __str__(self):

        for i in self.groups:
            return(i)
        #return f"Retrieving data for student {self.firstName} {self.lastName} (student ID {self.id})\n"+ \
        #    f"- GPA: {self.GPA} \n" + \
        #    f"- Major: {self.major} \n" +\
        #    f"- NHHS Group membership: {self.groups}"

    @property
    def listView(self):
        return f"{self.firstName} {self.lastName} (ID {self.id})"

        # Tanke: sjekk IF listen på membership er tom, i så fall "N/A"


student_dict = {
    19710 : Student(19710, "Mike", "Wheeler", 3.5, "FIE", ["it.gruppen"]),
    19670 : Student(19670, "Nancy", "Wheeler", 3.6, "ENE", ["K7 Bulletin", "NHHS Opptur", "NHHS Energi"]),
    19660 : Student(19660, "Steve", "Harrington", 2.4, "STR" ),
    18119 : Student(18119, "Mike", "Wazowski", 2.9, "BAN"),
    69420 : Student(69420, "Jeffrey", "Lebowski", 4.2, "BLZ", ["NHHI Bowling", "NHHI Vinum"]),
    12345 : Student(12345, "Ivan", "Belik", 1.8, "BAN", ["it.gruppen", "NHHS Consulting"]),
    11007 : Student(11007, "Sterling", "Archer", 2.7, "MBM", ["NHHI Lacrosse"])
}

# Create empty search dictionary
search_dict = dict()

def helper_add(value, id):
    """
    Helper function to add search terms (keys and values) to the
    search dictionary.
    Takes the ID from the student_dictionary to be used as value in search_dict,
    and "value" which would be the search term to be used as a key in search_dict.
    No return, just adds the key:value pair if the key didn't exist,
    or appends it to the list of values if the key already exists (i.e. multiple
    students with the same first/last name)
    """
    # If key does not already exist:
    if value not in search_dict:
        search_dict[value] = [id]     # Add to search_dict
    else: # If key already exists
        search_dict[value].append(id) # Append to existing list

# Adding entries to search_dict, with all searchable terms
# (first name, last name, first name and last name in any order,
# and finally student ID.
for id in student_dict:
    helper_add(student_dict[id].firstName, id)
    helper_add(student_dict[id].lastName, id)
    helper_add(student_dict[id].firstName + " " + student_dict[id].lastName, id)
    helper_add(student_dict[id].lastName + " " + student_dict[id].firstName, id)
    helper_add(id, id)


# ------------------ MAIN - fiks

def search_function(user_search):
    try:
        search_result = search_dict[user_search]
    except KeyError:
        return("No matches found.")
    else:
        if len(search_result) == 1:
            return(f"----------------\n"
                   f"One match found. \n" +
                   f"----------------\n" +
                   f"{student_dict[search_result[0]]}")
        else:
            print(f"Several results matched your query:")
            index = 1
            for id in search_result:
                print(f"{index}. {student_dict[id].listView}")
                index += 1

            input_control = True
            while input_control:
                user_choice = (input("Enter the number of the search result for " + \
                                        "which you want to retrieve the info or \n enter" + \
                                        " 'all' to print info for all matching results\n"))
                if user_choice.lower() == "all":
                    for id in search_result:
                        print(f"All search results: "
                            f"{student_dict[id]}")
                    input_control = False
                    return("----------------\n")
                else:
                    try:
                        user_choice = int(user_choice)
                        if user_choice < 1:
                            raise ValueError
                        chosen_student = search_result[user_choice-1]
                    except IndexError:
                        print("Incorrect input. Please try again.")
                    except ValueError:
                        print("Incorrect input. Please try again, with a number.")
                    else:
                        return(student_dict[chosen_student])
                        input_control = False






run_program = True
while run_program:
    user_search = input("Who are you looking for?\n").capitalize()
    print(search_function(user_search))

    while run_program:
        search_again = input("Would you like to search again? (y/n)\n")
        if search_again.lower() == "y":
            break
        elif search_again.lower() == "n":
            print("Exiting the program...")
            run_program = False
        else:
            print("Incorrect input. Please try again.")
