#!/usr/bin/python3
def uniq_add(my_list=[1, 2, 3, 1, 4, 2, 5]):
    uniq_list = set(my_list)

    for item in uniq_list:
        print(item)

    return uniq_list

if __name__ == "__main__":
    uniq_add()