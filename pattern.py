# def Pattern(n):
#     for i in range(n+1):
#         for j in range(i):
#             print("*",end=" ")
#         print()    
# Pattern(10)        

# def Pattern(n):
#     for i in range(n+1):
#         for j in range(1,i+1):
#             print(i,end=" ")
#         print()    
# Pattern(10)        
       
# def Pattern(n):
#     for i in range(n+1):
#         for j in range(1,n-i):
#             print("*",end=" ")
#         print()    
# Pattern(10)  

# def Pattern(n):
#     for i in range(n+1):
#         for j in range(1,(n+1)-i):
#             print(j,end=" ")
#         print()    
# Pattern(10) 

# def Pattern(n):
#     for i in range(n+1):
#         for j in range(1,(n+1)-i):
#             print(j,end=" ")
#         print()    
# Pattern(10) 

def Pattern2(n):

    for i in range(1, (2*n-1)+1):
        s=i
        if i>n:
            s=2*n-i
        for j in range(1,s+1):
            print("*",end=" ")     

        print()    

Pattern2(5) 



 