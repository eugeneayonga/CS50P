# LISTS
students = ["Hermoine", "Harry", "Ron", "Hagrid", "Ginny", "Neville", "Draco"]

for i in range(len(students)):
    print(i + 1, students[i])

print("**************************")

# DICTIONARIES
westerosi = {
    "Khaleesi": "Dragonstone", 
    "Arya": "Winterfell", 
    "Cersei": "King's Landing", 
    "Jon": "The Wall", 
    "Tyrion": "Casterly Rock"
}

for westeros in westerosi:
    print(westeros, westerosi[westeros], sep=": ")


print("**************************")
print("**************************")


# Dictionaries with lists
states = [
    {"name": "Florida", "capital": "Jacksonville", "Nickname": "Sunshine State"},
    {"name": "New York", "capital": "Albany", "Nickname": "New York State"},
    {"name": "California", "capital": "Sacramento", "Nickname": "Golden State"},
    {"name": "Texas", "capital": "Austin", "Nickname": "Lone Star State"},
    {"name": "Hawaii", "capital": "Honolulu", "Nickname": "Aloha State"},
    {"name": "Wahington D.C.", "capital": "Washington", "Nickname": None}
]


for state in states:
    print(state["name"], state["capital"], state["Nickname"], sep=": ")