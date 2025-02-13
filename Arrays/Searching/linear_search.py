def linear_search(nums,target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i
    return -1
nums = [1,2,3,4,5,6,7]
print(linear_search(nums,0))    
# best case o(1)
#Worst Case for traversing all element O(n) 