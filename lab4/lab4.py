# Write a program to print absolute value of a number entered by user. E.g.-
# INPUT: 1        OUTPUT: 1
# INPUT: -1        OUTPUT: 1
b=int(input("Enter a number."))
if b < 0:
    print(b*-1)
else:
    print(b)