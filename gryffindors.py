students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"}
]

def is_gryffindor(student):
    return student["house"] == "Gryffindor"


gryffindors = filter(is_gryffindor, students) # filter returns an iterator

for gryffindor in sorted(gryffindors, key=lambda student: student["name"]):
    print(gryffindor["name"])



# Dictionary Comprehension
scholars = ["Hermione", "Ron", "Harry"]

gryff = {scholar: "Gryffindor" for scholar in scholars}

print(gryff)


# Enumerators
clubs = ["Manchester United", "Liverpool", "Arsenal"]

for i, club in enumerate(clubs): # enumerate returns an enumerator
    print(i + 1, club)