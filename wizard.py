class Wizard:
    def __init__(self, name):
        self.name = name
        if not name:
            raise ValueError("Name cannot be empty.")

        ...
    
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

        ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

        ...


student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Dark Arts")

