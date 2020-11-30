class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = (98,78,88,99)

    def avarage_grades(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Person: {self.name}, {self.age} years old"

    def__repr__(self):

student = Student('bob', 35)
kevins_avg = student.avarage_grades()
print(student)
##########XXXXXXXXX######################XXXXXXXXX############
class Book:
    TYPES = ('hardcover', 'paperback')  

    def__init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def__repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g"
    
    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> 'Book':
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> 'Book':
        return cls(name, cls.TYPES[1], page_weight)