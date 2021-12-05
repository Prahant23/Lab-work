# Given the integer N - the number of minutes that is passed since midnight - how many

# hours and minutes are displayed on the 24h digital clock?
p = int(input("enter the integer N: "))
hour = p//60
minutes = p % 60
print(hour,minutes)
