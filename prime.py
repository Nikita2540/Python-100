def is_prime(n):
    if n<=1:
        print("This is not a prime number")
        return
    x=n-1
    while x>1:
            if n%x!=0:
              x-=1
            else:
                print ("It is Not a prime number")
                return
    print("This is a prime number")
    

number = int(input("Give me a number "))
is_prime(number)