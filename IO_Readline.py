f = open("test.txt", "rt")
#readline() function prints the line present in the file as each line \n at the it automatically prints a new line after each call.
print(f.readline())
print(f.readline())
print(f.readline())

#readlines() function stores the lines in a list and when we print it ,
#Its gives an list of the lines as the output.
print(f.readlines())

f.close()
