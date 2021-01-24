#  Health Management system
#  3 clients
#  What we need:
#  Total 6 files
#  A function that when executed takes as input client name
#  A function to retrives exercise or food for any clients
def getdate():
    import datetime
    return datetime.datetime.now()

import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c = int(input("Enter 1 for exercise and 2 for diet : "))
        if(c==1):
            value = input("Type here\n")
            with open("Shubham-ex.txt","a") as op:
                op.write(str([str(gettime())])+":" +value+ "\n")
            print("Succesfully Written")
        elif(c==2):
            value = input("Type here\n")
            with open("Shubham-food.txt", "a") as op:
                op.write(str([str(gettime())])+ ":" +value+ "\n")
            print("Succesfully Written")
    elif(k==2):
        c = int(input("Enter 1 fot exercise and 2 for diet : "))
        if(c==1):
            value = input("Type here\n")
            with open("Aman-ex.txt", "a") as op:
                op.write(str([str(gettime())])+ ":" +value+ "\n")
            print("Successfully Written")
        elif(c==2):
            value = input("Type here\n")
            with open("Aman-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" +value + "\n")
            print("Succesfully Written")
    elif(k==3):
        c = int(input("Enter 1 fot exercise and 2 for diet : "))
        if(c==1):
            value = input("Type here\n")
            with open("Rahul-ex.txt", "a") as op:
                op.write(str([str(gettime())])+ ":" +value+ "\n")
            print("Successfully Written")
        elif(c==2):
            value = input("Type here\n")
            with open("Rahul-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" +value + "\n")
            print("Succesfully Written")
    else:
        print("Please enter a valid input : ")
def retrieve(k):
    if k==1:
        c=int(input("Enter 1 for exercise and 2 for diet : "))
        if (c==1):
            with open("Shubham-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif(c==2):
            with open("Shubham-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k==2:
        c=int(input("Enter 1 for exercise and 2 for diet : "))
        if (c==1):
            with open("Aman-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif(c==2):
            with open("Aman-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k==2:
        c=int(input("Enter 1 for exercise and 2 for diet  : "))
        if (c==1):
            with open("Rahul-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif(c==2):
            with open("Rahul-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Please enter a valid input")
print("Health Management System: ")
a=int(input("Press 1 for giving input and 2 for seeing the the current status : "))

if a==1:
    b= int(input("Press 1 for Shubham, 2 for Aman & 3 for Rahul : "))
    take(b)
else:
    b= int(input("Press 1 for Shubham, 2 for Aman & 3 for Rahul : "))
    retrieve(b)
