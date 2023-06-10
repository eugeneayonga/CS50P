names = []
           
# Open the "students.txt" file in read mode and assign it to the variable 'file'
with open("students.txt", "r") as file:
    # Iterate over each line in the file
    for line in file:
        # Remove any trailing whitespace from the line and append it to the 'names' list
        names.append(line.rstrip())

        
    
for name in sorted(names): # sorted() is a built-in function that sorts a list
    print(f"Hello, {name}") 