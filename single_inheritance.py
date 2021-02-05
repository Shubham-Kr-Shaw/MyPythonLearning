
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole, aaddress):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.address = aaddress
    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary}, role is {self.role} and address is {self.address}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


class Programmer(Employee):
    no_of_holiday = 56
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages


    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"



harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Programmer("Shubham", 555, "Programmer", ["python"])
karan = Programmer("Karan", 777, "Programmer", ["python", "Cpp"])
print(karan.no_of_holiday)
