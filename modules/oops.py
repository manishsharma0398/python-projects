"""learning oops concepts"""


class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    def get_salary(self):
        return f"{self.name}'s salary is {self.salary}"


obj1 = Employee("Rohan", 15_000)
print(obj1.get_salary())
