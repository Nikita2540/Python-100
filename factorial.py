def factorial(n):
    factor = 1
    for i in range(n,0,-1):
        factor *=i
    return factor

number = int(input("Give us a number? "))
print (f"{factorial(number)}")