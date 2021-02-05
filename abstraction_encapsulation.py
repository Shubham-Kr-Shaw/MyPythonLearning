class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The name is {self.name}. Salary is {self.salary}. Role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

Shubham = Employee("Harry", 45665, "Programmer")
Aman = Employee("Aman", 45645, "Data Scientist")
Rahul = Employee.from_dash("Rahul-45452-Programmer")

Employee.printgood("Rohan")
print(Shubham.salary)
print(Rahul.printdetails())
