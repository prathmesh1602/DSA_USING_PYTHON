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

# def Pattern2(n):

#     for i in range(1, (2*n-1)+1):
#         s=i
#         if i>n:
#             s=2*n-i
#         for j in range(1,s+1):
#             print("*",end=" ")     

#         print()    

# Pattern2(5) 


# def pattern(n):
#     s=2*(n-1)
#     for i in range(1,n+1):
        
#         #number
#         for j in range(1,i+1):
#             print(j,end =" ")

#         #space
#         for j in range(1,s+1) :
#             print(" ",end=" ")
#         #number 
#         for j in range(i,0,-1) :
#             print(j,end=" ")   
            
#         print()
#         s-=2

       
# pattern(5)  

# def pattern(n):
#     s=1
#     for i in range(1,n+1):
#         for j in range(i):
#             print(s,end=" ")
#             s+=1
#         s=s   
#         print()     
# pattern(5)      

def pattern(n):
    if n <= 26:
        chr="ABCDEFGHIJKLMNOQURSTUVWXYZ"
        index=0
        for i in range(1,n+1):
            for j in range(i):
                print(chr[index],end=" ")
            index+=1
            print()  
    else:
        print("Please enter value less than 27")      
    
    
           
pattern(26)                                  
 