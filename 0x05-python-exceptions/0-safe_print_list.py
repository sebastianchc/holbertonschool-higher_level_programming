#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for elements in my_list:
            if count < x:
                print("{}" .format(elements), end="")
            else:
                break
            count += 1
    except:
        count = 1
    print("")
    return(count)
