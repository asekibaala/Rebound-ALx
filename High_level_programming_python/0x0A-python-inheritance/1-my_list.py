#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
