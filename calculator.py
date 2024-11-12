x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x/y, 3)

#you can also you the special f string to do round off
#print(f"{z:.3f}")  

print("Division of x by y will be", z, sep=": ")