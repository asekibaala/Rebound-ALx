#!/usr/bin/python3
print("Best School")

s = "hello"
print(s)  # Output: hello
print(id(s))  # Print the memory address of the original string

# Trying to change the first character of the string
s = "j" + s[1:]
print(s)  # Output: jello
print(id(s))  # Print the memory address of the new string
