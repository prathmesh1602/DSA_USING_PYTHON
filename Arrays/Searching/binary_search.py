def binary_search(arr,target): #Time Complexity: O(log n) 
                               #Space Complexity: O(1)
    left=0
    right = len(arr)-1

    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            left = mid +1 # move to the right half of array
        else:
            right = mid -1 # move to the left half of array
    return -1 

arr = [1,2,3,4,5,6,7,8]           
print(binary_search(arr,9)) 