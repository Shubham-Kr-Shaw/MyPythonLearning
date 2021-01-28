# args stands for arguments. It is used to unpack an argument.
# In the case of *args, the argument could be a list or tuple.

# some lines of code without using *args.
def functionToPrint(a, b, c, d):
    print(a, b, c, d)
functionToPrint("Aman","Shubham","Nikhil","Rishabh")#,"Extra")
# In this program every thing is working fine but the prpblem starts when we pass an extra argument it throws an error as given below.
# functionToPrint() takes 4 positional arguments but 5 were given

# Now using the *args
def funargs(normal, *args):
    print(normal)
    for item in args:
        print(item)

normal = "\nName of the people working together are : "
name = ["Aman","Shubham","Nikhil","Rishabh"]

funargs(normal, *name)

# Now using the **kwargs, "kwargs" stands for "Keyword Arguments"

def funargs1(normal, **kwargs):
    print(normal)
    for key,value in kwargs.items():
        print(f"{key} is a {value}")

normal = "\nName of the people working With there respective roles assigned : "
kwname = {"Aman":"Data Scientist","Shubham":"ML Engineer","Nikhil":"Backend Developer","Rishabh":"DevOps Engineer"}
funargs1(normal, **kwname)
