tribes = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Luna", "house": "Ravenclaw"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Cedric", "house": "Hufflepuff"},
    {"name": "Fred", "house": "Gryffindor"},
    {"name": "Ginny", "house": "Gryffindor"},
    {"name": "Severus", "house": "Slytherin"}
]

houses = set()

for tribe in tribes:
    houses.add(tribe["house"])

for house in sorted(houses):
    print(house)