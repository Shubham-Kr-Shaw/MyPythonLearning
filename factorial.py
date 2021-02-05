def factorial(num):
    return 1 if (num==1 or num==0) else num * factorial(num-1)


n = int(input("Enter a number to find its factorial: "))
f = factorial(n)
print(f"Factorial of {n} = {f}")
