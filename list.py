animal = ["Dog", "Cat", "Cow", "Lion"]
print(animal)
numbers = [1, 2, 3, 4, 8, 6, 7, 8, 9]
numbers.append(88)
numbers.insert(1, 55)
numbers.pop()
print(numbers)
print(numbers[::-1])  # It reverse the  content of the list

"""  
__________|_____________________________
Method	  |    Description
----------|-------------------------------
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index() 	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""
# We have one more variation of list i.e. tuple the main difference is the content of the list is mutable but the content of tuple is immutable.

tp = (5, 4, 3, 2, 1)
# tp[1]=2 # this line will give an Error because ewe can not change the value of the content of a tuple
print("\nThis is a tuple")
print(tp, "Its value can't be manipulated")

# An interesting program
print("How we do on other swap the value of two variables in other languages")
a = 5
b = 6
print (a, b, "Before swap")
temp = a
a = b
b = temp
print(a, b, "After swap")

print("How we swap the value of two variable in python")
print(" x, y = y, x LOL ")
x = 1
y = 0
print(x, y, "Before swap")
x, y = y, x
print(x, y,  "After swap")



