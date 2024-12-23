def list_sort(list):
    x=len(list)
    if x<=1:
        print("Your list is empty or have only one element")
        return list
    else:
        for i in range (0,x):
            for j in range(x-i):
                if list[x-j-1]>list[x-j-2]:
                    continue
                else:
                    list[x-j-1], list[x-j-2] = list[x-j-2], list[x-j-1]
    return list

list_1 = []

print(list_sort(list_1))