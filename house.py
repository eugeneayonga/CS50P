name = input("What's your name? ")

match name:
    case "Daenerys" | "Aemon" | "Viserys":
        print("House Targaryen")
    case "Jon":
        print("House Snow")
    case "Arya":
        print("House Stark")
    case "Tyrion" | "Cersei" | "Jaime":
        print("House Lannister")
    case "Stannis":
        print("House Baratheon")
    case "Samuel":
        print("House Tarly")
    case _:
        print("Go away, peasant.")

# if name == "Daenerys" or name == "Aemon" or name == "Viserys":
#     print("House Targaryen")
# elif name == "Jon":
#     print("House Snow")
# elif name == "Arya":
#     print("House Stark")
# elif name == "Tyrion" or name == "Cersei" or name == "Jaime":
#     print("House Lannister")
# elif name == "Stannis":
#     print("House Baratheon")
# elif name == "Samuel":
#     print("House Tarly")
# else:
#     print("Go away, peasant.") # this is the else statement
