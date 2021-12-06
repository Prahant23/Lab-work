# . Given a n-digit number. Find the sum of its digits.

p = int(input("Enter a number: "))
total = 0
while p>0:
    digits=p%10
    total=total+digits
    number=p//10
print("The sum of digits of the number entered is",total)

