n = int(input("Enter the dimention for the pattern :"))

for i in range(0, n):
    for j in range(0, i+1):
        print("* ",end="")
    print("\r")
