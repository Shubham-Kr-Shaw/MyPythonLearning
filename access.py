class Student:
    klass = "10th"
    subjects = "Maths"
    _rollNo = "roll"
    __marks = 75

    def __init__(self, nname, ssection, _rroll):
        self.name = nname
        self.section = ssection
        self._roll = _rroll

    def printdetails(self):
        return f"The name is {self.name}. Class is {self.klass}Section is {self.section}.Roll no is{self._roll}"

student1 = Student("Sonu", "A", "28")
print(student1.printdetails())
print(student1._Student__marks)
