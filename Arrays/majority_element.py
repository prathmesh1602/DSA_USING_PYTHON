#Brute Force approch
# def majority_element(arr):
#     arr.sort()
#     fre = 0
#     for i in arr:
#         if i == i:
#             fre+=1
           
#         if fre > len(arr)//2:
#             return i
# arr = [1,2,2,1,1,2]
# print(majority_element(arr))        


# More Optimize Alogorithm (Moore's voting Algo)
def majority_element(arr):
    count = 0 
    candidate =  0

    for num in arr :
       
        if count == 0:
            candidate = num
         
        if num == candidate:
            count+=1
                
        else:
            count-=1
            
    return candidate
arr = [2,2,1,1,1,2,2,1,1]
print(majority_element(arr))                 