def sort(list):
    empty_list = []
    limit=len(list)
    for i in range(limit):
        minima = min(list)
        empty_list.append(minima)
        list.remove(minima)
    return empty_list

def get_list():
    user_list = []
    num = int(input("how many elements do you want in the list?"))
    for i in range(num):
        n = int(input(f"what's the element no. {i+1}? "))
        user_list.append(n)
    return user_list


list_1 = get_list()
print(sort(list_1))