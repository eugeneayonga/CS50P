# LOOPS

"""
# while loop
i = 3
while i != 0:
    print("meow!")
    i -= 1 # this is the same as i = i - 1 # decrementing

a = 0
while a < 3:
    print("mooo!")
    a += 1 # this is the same as a = a + 1 # incrementing

# for loop
for _ in range(3): # _ is a throwaway variable
    print("Roar!")

cities = ["Nairobi", "Kisumu", "Mombasa", "Nakuru"]
for city in cities:
    print(city)

while True:
    n = int(input("Enter a number: "))
    if n > 0:
        break # this will break out of the loop

for _ in range(n):
    print("Crow!")
"""


def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            break
    return n
        

def meow(n):
    for _ in range(n):
        print("meow!")

main()