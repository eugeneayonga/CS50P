def main():
    print_column(5)
    print_row(5)
    print_square(10)
    

def print_column(height):
    for _ in range(height):
        print("#")

def print_row(width):
    print("?" * width)

def print_square(size):
    # For each row in square
    for i in range(size):
        # For each brickin row
        for j in range(size):
            # printbrick
            print("#", end="")
        # print newline
        print()

main()