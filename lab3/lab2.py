# WAP which accepts marks of four subjects and display total marks,
#percentage and grade. Hint: more than 70% –> distinction, more than 60% –> first,
# more than 40% –> pass, less than 40% –> fail
a = int(input("enter a first subject marks: "))
b = int(input("enter a second subject marks: "))
c = int(input("enter a third subject marks: "))
d = int(input("enter a fourth subject marks: "))
total_marks = (a+b+c+d)
print(total_marks)
percentage = (total_marks/400*100)
if percentage<=70:
    print("you got distinction")
elif percentage<=60:
    print("first")
elif percentage<=40:
    print("second")
else:
    print("fail")







