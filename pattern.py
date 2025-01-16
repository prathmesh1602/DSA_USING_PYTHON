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
def Pattern1(n):
    for i in range(n):
         
        
        for k in range(i*2+1):
            print("*",end=" ")
        for l in range(n-i-1):
            print(" ",end=" ")        

        print()    
Pattern1(4) 

def Pattern2(n):

    for i in range(n,0,-1):
         
       
        for k in range(i*2-1):
            print("*",end=" ")
        for l in range(n-i):
            print(" ",end=" ")  
                   

        print()    

Pattern2(4) 



 