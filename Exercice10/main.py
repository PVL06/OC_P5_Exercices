class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def display_details(self):
        print(f"{self.name}, {self.age}")


class Employee(Person):
    def __init__(self, name, age, salary) -> None:
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        super().display_details()
        print(self.salary)


e = Employee("john", 32, 2300)
e.display_details()
