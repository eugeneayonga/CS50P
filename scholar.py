class Scholar:
    def __init__(self, name, house):        
        self.name = name
        self.house = house
        
    def __str__(self):
        return f"{self.name} of house {self.house}."
    
    @classmethod
    def get(cls):
        name = input("Name: ") 
        house = input("House: ")
        return cls(name, house)

def main():
    scholar = Scholar.get()
    print(scholar)


if __name__ == "__main__":
    main()