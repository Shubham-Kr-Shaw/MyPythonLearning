#  dictionary is a key value pairs

d1 = {"Veg": "Paneer Chilly", "Non-veg": "Chicken Tandoori", "Main course": "Biryani", "Desert": "Ice cream"}
d2 = {"Pen": "Rs.10", "Pencil": "Rs.5", "Book": "1500"}
print(d1, '\n', d2)
d1.clear()
print(d1)
d3 = d2.copy()
print(d3)

"""
_____________|_________________________________________
Method	     |       Description
-------------|-----------------------------------------
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()     	Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()   	    Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
 
"""