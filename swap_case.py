def swapc(a):
    # return a.swapcase()
    new = ""
    for i in range(len(a)):
        if str.islower(a[i]):
            new = new + str.upper(a[i])
        elif str.isupper(a[i]):
            new = new + str.lower(a[i])
        else:
            new = new + str(a[i])
    return (new)


if __name__ == '__main__':
    s = input("Enter a string to alter the case in which it is written: ")
    #This is a inbuilt method swapcase() which alters the case of the string.
    #The Swaping of the case can also be done by the above method by changing the case of each letter of the string by iterating and changing the case of each letter.
    print(s.swapcase())
    print(swapc(s))
