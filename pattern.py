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

def Pattern(n):
    for i in range(n+1):
        for j in range(1,(n+1)-i):
            print(j,end=" ")
        print()    
Pattern(10) 
