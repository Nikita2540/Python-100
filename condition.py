def main():
    x=int(input("Give me a number "))
    is_even(x)

def is_even (n):
    if n==0:
        print("This is an even number")
    elif n%2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number")

main()