def main():
    x = input("What's x? ")
    print("x squared is", square(x))

def square(n):
    return n * n

if __name__ == "__main__": # If this file is run directly, run main() # If this file is imported, don't run
    main()