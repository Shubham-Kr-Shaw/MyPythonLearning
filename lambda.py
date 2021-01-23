"""
We use lambda functions when we require a nameless function for a short period of time.
In Python, we generally use it as an argument to a higher-order function (a function that takes in other
functions as arguments).Lambda functions are used along with built-in functions like filter() , map() etc.
"""

#Lambda arguments: expression
x = lambda a: a*a
print(x(3))#Calling tha lambda function

#A normal user defined function
def sq(s):
    return s*s

i=int(input("Enter a no to find it's square : "))
print("Square of ", i ,"=", sq(i))#Calling and printing the return value of user defined function

#A user defined function within which a lambdafunction is also used
def a(x):
    return(lambda y:x+y)
t=a(5)
print(t(6))

#Lambda within filter()
#Syntax: filter(function,iterables)
oldlist = [1,2,3,4,5,6,7,8,9,10]
newlist = list(filter(lambda a:(a%2==0), oldlist))
print(newlist)

Lambda within the map()
Syntax: map(function,iterables)
oldlist = [1,2,3,4,5,6,7,8,9,10]
newlist = list(map(lambda a:(a%2==0), oldlist))
print(newlist)

#Lambda within the reduce()
#Syntax: reduce(function,sequence)
from functools import reduce
print(reduce(lambda a,b: a+b,[1,2,3,4,5,6,7,8,9,10]))

#Lambda function for Algebra
#Linear eq
s = lambda a,b:5*a+7*b
print(s(2,5))

#Quadratic eq(a+b)^2
sq = lambda a,b:(a+b)**2
print(sq(3,4))
