


def revernumber(n):
    rev = 0
    temp=0
    is_negativ = False
    
   
    if n < 0:
        is_negativ = True
        n = n*-1

    while n != 0:
        rev = n%10
        temp = (temp*10)+rev
        n = n//10
        
    if temp < -2**31 or temp > 2**31 - 1:
        return 0    
    return -temp if is_negativ else temp

print(revernumber(1534236469))    