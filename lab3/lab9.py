#  Take username and password from user and check it again for the three times
username = str(input("enter your name"))
password = str(input("enter you password"))


for i in range(0, 3):
    x = str(input("enter your username"))
    y = str(input("enter your password"))
    if x == username and y == password:
        print("login successful")
        break
    elif i < 3:
        if x != username and y != password and i < 3:
            print("invalid credentials")
else:
    print("exceeded 3 attempts")
