# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# right = k
# left = 0
# n = len(nums)
# ans = []

# while left < right and right < n+1:
#     new_nums = nums[left:right]
#     ans.append(max(new_nums))
#     left+=1
#     right+=1

# print(ans)    

l= [1,1.2,True,"Hello"]
for i in l:
    print(id(i))