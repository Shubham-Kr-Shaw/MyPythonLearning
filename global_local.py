#There are 2 types of variable, i.e global and local variable
glo = 10 #Global
def function1(n):
    loc1 = 8 #Local
    global glo
    glo = loc1 #This is a local variable but using "global" keyword we can change the value of the global variavle
    print(n, "This is the output of the method: ", loc1, glo)

function1("Calling the Method: ")
print("This is the output outside the method")
print(glo)
# print(loc1)
