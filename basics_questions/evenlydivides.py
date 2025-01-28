def evenlydivides(n):
    r =0
    temp = n
    count = 0
    while n != 0:
        r = n%10
        if r != 0:
            if temp%r == 0:
                count = count+1
            
        n = n//10
    if count == 0:
        return 0
    else:
        return count

print(evenlydivides(23))            