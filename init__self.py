class Employee:
    no_of_leaves = 6

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The name is {self.name}. Salery is {self.salery} and role is {self.role}"

emp1 = Employee("Shubham", 255, "Instructor")
emp2 = Employee("Rahul", 345, "Teacher")

print(emp1.name)
