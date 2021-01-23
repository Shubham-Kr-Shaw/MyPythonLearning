n = int(input("Enter the dimention for the pattern :"))
character= input("Enter the character u want to print pattern : ") 
# to take a chararcter alsoas input 

for i in range(0, n):
    for j in range(0, i+1):
        print(character,end="")
    print("\r")
