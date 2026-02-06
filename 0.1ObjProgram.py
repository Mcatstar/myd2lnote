class Person:

    max_age = 120  # Class variable representing maximum age
    def __init__(self, name, age, gender=None, id_number=None):
        self.name = name # Public attribute
        if age > Person.max_age:
            self.age = Person.max_age
            print(f"Age cannot be greater than {Person.max_age}.")
        else:
            self.age = age
        self._gender = gender # Protected attribute
        self.__id_number = id_number # Private attribute

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    @property
    def getgender(self):
        return self._gender
    @getgender.setter
    def setgender(self, gender):
        self._gender = gender
    @property
    def get_id_number(self):        
        return self.__id_number
    @get_id_number.setter
    def set_id_number(self, id_number):
        self.__id_number = id_number
    
    # 魔法方法
    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age}, Gender: {self._gender}, ID Number: {self.__id_number})"
    def __len__(self):
        return len(self.__dict__)
    def __getattr__(self, name):
        return f"{name} is not found."
class Student(Person):
    def __init__(self, name, age, student_id, gender=None, id_number=None):
        super().__init__(name, age, gender, id_number)
        self.student_id = student_id
    
# Example usage:
if __name__ == "__main__":
    print(Person)
    print("{:-^64}".format("person1"))
    person = Person("Alice", 30)
    print(person)
    print(person.__dict__)
    print(person.greet())   # Output: Hello, my name is Alice and I am 30 years old.
    person.setgender = "Female"
    print(" Gender:", person.getgender)
    person.set_id_number = "ID123456"
    print(" ID Number:", person.get_id_number)
    print(person.__len__())  # Output: 4
    print(person.address)  # Output: address is not found.
    print("{:-^64}".format("person2"))
    person2 = Person("Bob", 130)  # This will raise a ValueError
    print(person2.age)  # Output: 120
    print("{:-^64}".format("student1"))
    student = Student("Charlie", 20, "S12345")
    print(student)
    print("studentObj isinstance:",isinstance(student, Person))  # Output: True
    print("StudentClass issubclass",issubclass(Student, Person))  # Output: True
    print(Student.__mro__)  # Output: (<class '__main__.Student'>, <class '__main__.Person'>, <class 'object'>)
    print(student.__dict__)
    print(student.greet())  # Output: Hello, my name is Charlie and I am 20 years old.

