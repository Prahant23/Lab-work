#4. Given three integers, print the smallest one. (Three integers should be user input)

q = int(input("enter first integer: "))
w = int(input("enter second integer: "))
e = int(input("enter third integer: "))
if q<w<e:
    print(" first integer is smaller")
elif w<q<e:
    print("second integer is smaller")
else:
    print("third integer is smaller")