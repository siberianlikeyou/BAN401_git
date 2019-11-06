
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

for id in student_dict:
    helper_add(student_dict[id].firstName, student_dict[id])
    helper_add(student_dict[id].lastName, student_dict[id])
    helper_add(student_dict[id].firstName + " " + student_dict[id].lastName, student_dict[id])
    helper_add(student_dict[id].lastName + " " + student_dict[id].firstName, student_dict[id])
    helper_add(id, student_dict[id])

    # Create dict with all student objects
    student_dict = {
        19710: Student(19710, "Mike", "Wheeler", 3.5, "FIE", ["it.gruppen"]),
        19670: Student(19670, "Nancy", "Wheeler", 3.6, "ENE", ["K7 Bulletin", "NHHS Opptur", "NHHS Energi"]),
        19660: Student(19660, "Steve", "Harrington", 2.4, "STR"),
        18119: Student(18119, "Mike", "Wazowski", 2.9, "BAN"),
        69420: Student(69420, "Jeffrey", "Lebowski", 4.2, "BLZ", ["NHHI Bowling", "NHHI Vinum"]),
        12345: Student(12345, "Ivan", "Belik", 1.8, "BAN", ["it.gruppen", "NHHS Consulting"]),
        11007: Student(11007, "Sterling", "Archer", 2.7, "MBM", ["NHHI Lacrosse"])
    }