# def pow(x,n):
#     result = 1
#     for _ in range(abs(n)):
#         result *=x

#     if n <  0:
#         result = 1/result

#     return result
# print(pow(2,-3))    

# More Optimize approch
def pow(x,n):
    if n == 0:
        return 1 
    elif n<0:
        x=1/x
        n=-n # for convert negativ n to positiv n
    result = 1
    while n > 0 :
        if n %2 == 1:
            result *=x
        x*=x
        n//=2


    return result
x=2
n=10
print(pow(2,10))     

