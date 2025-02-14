def majaority_element(nums):
    n = len(nums)
    dic = {}
    temp =[]
    mini = (n//3)
    count = 0
    for i in range(len(nums)):
        dic[nums[i]] = count
        if nums[i] == dic[nums[i]]:
            count+=1
             dic[nums[i]] = count    
        
    print(dic)
       
    
l = [1,1,1,3,3,2,2,2]
print(majaority_element(l))               
    
                
