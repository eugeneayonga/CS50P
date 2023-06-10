name = input("What's your name? ")

with open("students.txt", "a") as file: # "a" stands for append # "w" stands for write
    file.write(f"{name}\n") # this is the way to write to the file

