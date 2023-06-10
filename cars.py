import csv

make = input("Enter the model of the car: ")
model = input("Enter the make of the car: ")

with open("cars.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["make", "model"])
    writer.writerow({"make": make, "model": model})
