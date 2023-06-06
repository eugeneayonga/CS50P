def main():
    name = input("What's your name? ")
    hello(name)

# function
def hello(to_whom = "World!"):
    print("Hello!", to_whom)

main()