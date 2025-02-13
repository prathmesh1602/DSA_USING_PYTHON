def lagest(arr):
    n = len(arr) # O(1) (constant time)
    if n == 1:#O(1)
        return arr[0]
    else:
        max_val = arr[0]
        for i in range(n): #O(n)
            if arr[i] > max_val:
                max_val = arr[i]
    return max_val
arr = [1,5,7,12,34,6]   
print(lagest(arr))         

# Overall Time Complexity O(n)
# Space Complexity O(1) 
# function doesh not create any additional data stucture