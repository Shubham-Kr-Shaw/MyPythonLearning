class Employee:
    department = "SDE"
    timing = "9-5" #class variables

emp1 = Employee()
emp2 = Employee()

emp1.id = 1 #instance variables or object variables
emp1.name = "Shubham"
emp1.salery = 3000
emp1.role= "SDE"

emp2.id = 2
emp2.name = "Rahul"
emp2.salery = 3000
emp2.role = "MLE"
emp2.timing = "10-6" # this creats a new instance variable but does not changes the value of class variable.

print(Employee.__dict__, "\n")
print(emp2.__dict__)
print(emp2.timing)
