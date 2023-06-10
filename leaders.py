# Import the csv module to read the data from a csv file.
import csv

# Initialize a list to hold the leaders' data.
leaders = []

# Open the csv file for reading.
with open("leaders.csv", "r") as file:
    # Create a csv reader object.
    reader = csv.DictReader(file)

    # Sort the rows in the csv file by the "name" field.
    sorted_reader = sorted(reader, key=lambda row: row["name"])

    # Iterate over the rows in the sorted csv reader object and add 
    # the leaders' data to the list.
    for row in sorted_reader:
        leaders.append({"name": row["name"], "home": row["home"]})

# Iterate over the leaders' data and print out each leader's name and home.
for leader in leaders:
    print(f"{leader['name']} is from {leader['home']}")
