s = set([1, 2, 3])
print("We can se that the datatype is ", type(s))
#  It may look like list but in set only unique items can be stored
#  We can add items by using add() method
s.add(4)
s.add(5)
s.add(6)
s.add(7)
s.add(8)
s.add(9)
print("s set is", s)
lst = [9, 10, 11, 10]  # This is a list which can contain duplicate items
print("List with multiple duplicate items", lst)
s1 = set(lst)  # When we put the list into the set it implicitly ignores the duplicate items
print("s1 set is", s1)
print("Union of set s & s1", s.union(s1))
print("This methods return the length of the set:", len(s))
print("This tells weather the 2 sets are disjoint or not", s.isdisjoint(s1))
print("Intersect of the two sets is", s.intersection(s1))
"""
Built-in methods that you can use on sets.
_____________________________________________________________
Method           |          	Description
-------------------------------------------------------------
add()	                Adds an element to the set
clear()	                Removes all the elements from the set
copy()	                Returns a copy of the set
difference()	        Returns a set containing the difference between two or more sets
difference_update() 	Removes the items in this set that are also included in another, specified set
discard()	            Remove the specified item
intersection()	        Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	        Returns whether two sets have a intersection or not
issubset()	            Returns whether another set contains this set or not
issuperset()    	    Returns whether this set contains another set or not
pop()	                Removes an element from the set
remove()	            Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	                Return a set containing the union of sets
update()	            Update the set with the union of this set and others

"""