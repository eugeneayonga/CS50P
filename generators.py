def main():
    n = int(input("Enter a number: "))

    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * i # yield is like return, but it doesn't stop the function

if __name__ == "__main__":
    main()