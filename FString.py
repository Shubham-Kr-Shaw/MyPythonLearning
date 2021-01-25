# F String - It literally stands for Fast String.

# Different methods of string formating.
# 1.This type of string formiting works but
#It is not effective because of unconvenience if used with large no of variables.\
me = "Shubham"
print("My name is %s"%me)

# 2.In this we will pass a tuple of variables which will have some string stored in it.
# It is not efficient as well because it is not at all readable.
f = "Shubham"
l = "Shaw"
a = "My name is %s %s"%(f, l)
print(a)

# 3.In this we will pass the index of a tuple of variables which will have some string stored in it.
# It is not efficient as well because it is also not readable but can be used for some string manuplation operation.
f = "Shubham"
l = "Shaw"
a = "My name is {1} {0}"
b = a.format(f, l)
print(b)

# 4.Using F String here F stands for fast string.
import math
s1 = "Shubham"
s2 = "Kumar"
s3 = "Shaw"
print(f"My name is {s1} {s2} {s3}, and value of sin 30 = {math.sin(30)}")
