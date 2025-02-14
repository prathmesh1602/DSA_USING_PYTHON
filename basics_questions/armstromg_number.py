def armStrongNumber(num):
    sum = 0
    temp = num

    while temp > 0:
        rem = temp % 10
        sum = sum+(rem**3)
        temp = temp//10
    if sum ==  num:
        return True
    else:
        return False
num = 371
print(armStrongNumber(num))      