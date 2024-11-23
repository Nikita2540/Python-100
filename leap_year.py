def is_leap(year):
    if year%4==0: 
        if year%100==0:
            if year%400==0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    
    return leap

year = int(input("Let's check if a year is leap year or not, give me a year!! "))
if is_leap==True:
    print("It's a leap year")
else:
    print("This is not a leap year")
