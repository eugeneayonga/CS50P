def main():
    x = get_int("What's x? ")
    print(f"You've entered: {x}")
    
def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("That's not a number! Try again.") # pass can be used here
        else:
            break

    return x
    
        
main()
