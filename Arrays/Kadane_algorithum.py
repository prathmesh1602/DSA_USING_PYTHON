def max_subaarray_sum(arr):
    max_sum = float('-inf') # intialize with smallest possible value in negativ infinite
    current_sum = 0

    for num in arr:
        current_sum += num

        if current_sum > max_sum:# compare with max_sum if currrent_sum greater tham max_sum than max_sum updated
            max_sum = current_sum

        if current_sum < 0:# if the current_sum is less than 0, negativ number tham current_sum update to 0
            current_sum = 0

    return max_sum

arr = [1,-2,3,4,-5,6]
ans = max_subaarray_sum(arr)   
print(ans)             
 #Linear time O(n)
       