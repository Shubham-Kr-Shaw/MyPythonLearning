#f.seek(x) is a method by which we can move the file pointer to aur desiresd position
#f.tell() returns the position of the pointer
f = open("test.txt")
print(f.tell())
print(f.readline())
f.seek(15)
print(f.tell())
print(f.readline())
f.close()
