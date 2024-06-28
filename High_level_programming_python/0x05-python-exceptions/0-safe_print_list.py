#!/usr/bin/python3
def safe_print_list(mylist=[],x=0):
    count =0
    for i in range(x):
        try:
            print("{}".format(mylist[i]),end='')
        except:
            break
        else:
            count +=1
    print()
    return (count)