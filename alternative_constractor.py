class Student:
    no_of_subjects = 6

    def __init__(self, aname, aroll, asection):
        self.name = aname
        self.roll = aroll
        self.section = asection

    def printdetails(self):
        return f"The name is{self.name}.\nRoll no. is {self.roll},\nSection is {self.section}\n"

    @classmethod
    def change_subjects(cls,newsubject):
        cls.no_of_subjects = newsubject

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

shubham = Student("Shubham Kr", 1, "A")
mohit = Student("Mohit Paswan Kr", 2, "A")
rohit = Student("Rohit Kr", 3, "A")
rahul = Student("Rahul pandey", 4, "A")
karan = Student.from_dash("karan-5-A")

print(karan.section)
print(mohit.name)
print(rahul.no_of_subjects)

shubham.change_subjects(7)
print(rohit.no_of_subjects)
print(rahul.no_of_subjects)
