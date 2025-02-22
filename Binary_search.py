def find_middle (lower, upper):

    return int((lower+upper)/2)

    # diff = upper - lower + 1
    # if diff%2==0:
    #     middle = (((diff/2)+lower) + (((diff/2)+1)+lower))/2
    #     mid = round(middle)
    # else:
    #     middle = (((diff+1)/2)+lower)
    #     mid = round(middle) -1
    # return mid

def search(list,target):
    length = len(list)
    lower = 0
    upper = length-1
    if list[lower]==target:
        return lower
    elif list[upper]==target:
        return upper
    else:
        while(upper-lower!=1):
            if list[find_middle(lower, upper)] <target:
                lower = find_middle(lower, upper)
            elif list[find_middle(lower, upper)] >target:
                upper = find_middle(lower, upper)
            elif list[find_middle(lower, upper)]==target:
                return find_middle(lower, upper)
            else:
                return "Target is not in the given list"

def main():
    list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(search(list_1, 6))

if __name__=="__main__":
    main()



