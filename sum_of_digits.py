num = 0
def way_1():
    global num
    number = str(input("What's the number? "))
    for i in range (len(number)):
        num +=int(number[i])

def way_2():
    global num
    number = list(input("What's the number? "))
    x=0
    while x<len(number):
        num += int(number[x])
        x+=1
  
way= int(input("Which way do you want? 1 or 2? "))



if way==1:
    way_1()
else:
    way_2()


print(num)
