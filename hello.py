def main():
    name = input("What's your name? ")
    print(hello(name))

# function
def hello(to_whom = "World!"):
    return f"Hello!, {to_whom}"

if __name__ == "__main__":
    main()