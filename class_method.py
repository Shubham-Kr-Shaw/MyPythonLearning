class Employee:
    no_of_leaves = 6

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The name is {self.name}. Salery is {self.salery} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

Shubham = Employee ("Shubham Kr Shaw", 999, "Intern")
Aman = Employee ("Aman Pandey", 99999, "Data Scientist")

Aman.change_leaves(8)
print(Shubham.no_of_leaves)
