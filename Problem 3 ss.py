"""
Problem 3
"""
class Student:
    """
    DEFINE THIS
    """

    def __init__(self, id, firstName, lastName, GPA, major, groups):

        # Initialize variables
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.GPA = GPA
        self.major = major
        self.groups = groups

    # Using str magic method to create printable representation of Student
    def __str__(self):

        return f"Retrieving data for student {self.firstName} {self.lastName} (student ID {self.id})\n"+ \
            f"GPA: {self.GPA} \n" + \
            f"Major: {self.major} \n" +\
            f"NHHS Group membership: {self.groups}"





#test1 = Student(19710, "Mike", "Wheeler", 3.5, "FIE", ["it.gruppen"])

print(student_dict[19710])

student_dict = {
    19710 : Student(19710, "Mike", "Wheeler", 3.5, "FIE", ["it.gruppen"])
    


}