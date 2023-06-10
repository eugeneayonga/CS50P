# Create an empty list to hold the student data.
students = []

# Open the "students.csv" file in read mode.
with open("students.csv", "r") as file:

    # Iterate over each line in the file.
    for line in sorted(file):

        # Remove the newline character and split the line by comma.
        name, location = line.rstrip().split(",")

        # Create a dictionary to hold the student data.
        student = {}

        # Add the name and location data to the student dictionary.
        student = {"name": name, "location": location}

        # Append the student dictionary to the students list.
        students.append(student)

# Iterate over each student dictionary in the students list sorted by name.
for student in students:

    # Print the name and location data for each student.
    print(f"{student['name']} is in {student['location']}")
