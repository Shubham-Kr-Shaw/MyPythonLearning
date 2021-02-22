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
    print(s.swapcase())
    print(swapc(s))
