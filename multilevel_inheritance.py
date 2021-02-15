class Grandpa:
    lastname = "Shaw"
    apple = int(10)
    def Tapple(self):
        return f"I have {self.apple} apples"

class Papa(Grandpa):
    middlename = "Kumar"
    apple = int(10)
    def Tapple(self):
        Total_apple = int(self.apple + Grandpa.apple)
        return f"I have {Total_apple} apples."

class Son(Papa):
    firstname = "Shubham"
    apple = int(10)
    def Tapple(self):
        Total_apple = int(self.apple + Grandpa.apple + Papa.apple)
        return f"I have {Total_apple} apples."

Shubham = Son()
Suresh = Papa()
Narayan = Grandpa()

print(f"My name is {Narayan.lastname}, I am Grandpa of Shubham")
print(Narayan.Tapple())

print(f"My name is {Suresh.middlename} {Suresh.lastname}, I am papa of Shubham")
print(Suresh.Tapple())

print(f"My name is { Shubham.firstname} {Shubham.middlename} {Shubham.lastname}")
print(Shubham.Tapple())
