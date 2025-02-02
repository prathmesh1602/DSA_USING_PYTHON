def remove_duplicates(nums):
    n= len(nums)
    temp=nums[0]
    for i in range(n):
        for j in range(i+1,n):
            if nums[j] != nums[i]:
                nums[i+1] = nums[j]
    print(nums)            
        


l = [1,1,2,2,2,3,3,4]
remove_duplicates(l)    
