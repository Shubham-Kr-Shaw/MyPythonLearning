myStr = "Happy new year"
print(myStr)  # It prints the string
print(myStr[0:14])
# This is string slicing Where it by default takes the first value as 0 and end value as the length of the string
print(myStr[5:12])  # In slicing we can change the values of index as per the requirement
# Advance slicing
print(myStr[0:14:2])  # This is advance slicing where the last value is to skip 'n' no of characters
# if the index are on -ve value then it will be started from the end i.e. -1 index will point to the end of the string
print(myStr[-15:-1])
# Now one of the best way for inverting the string
print(myStr[::-1])

# Some popular methods
print(myStr.capitalize())
print(myStr.casefold())
print(myStr.upper())
print(myStr.count("a"))
print(myStr.endswith("YEAR"))
print(myStr.endswith("year"))
print(myStr.find("new"))
print(myStr.replace("new", "2021"))
print(myStr.index("y"))
print(myStr.isdigit())

"""
 Python has a set of built-in methods that you can use on strings.
 Note: All string methods returns new values. They do not change the original string.
 List of the most of the functions are-
_____________|_______________________________________________________
  Method 	 |             Description
-------------|-------------------------------------------------------
capitalize()	Converts the first character to upper case
casefold()	    Converts string into lower case
center()	    Returns a centered string
count()	        Returns the number of times a specified value occurs in a string
encode()	    Returns an encoded version of the string
endswith()   	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()       	Formats specified values in a string
format_map()	Formats specified values in a string
index()     	Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isdecimal() 	Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	    Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle()	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()	        Joins the elements of an iterable to the end of the string
ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	    Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()	    Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	        Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
translate()	    Returns a translated string
upper()	        Converts a string into upper case
zfill()	        Fills the string with a specified number of 0 values at the beginning
 
"""