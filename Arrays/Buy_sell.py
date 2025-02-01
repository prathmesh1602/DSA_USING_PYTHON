def max_profit(arr):
    n= len(arr)
    max_profit = 0 # intitilize max_profilt = 0
    best_buy =arr[0] # best_buy start from day 0
    for i in range(n):
        print("day_price",arr[i])
        if arr[i] > best_buy: # if day_price is grater than best_buy
            max_profit = max(max_profit,arr[i]-best_buy) # update profit by comparing current max_profit and day_price-best_buy
            print("max_profit",max_profit)
        best_buy = min(best_buy,arr[i])
        print("best_buy",best_buy)
    return max_profit    
arr = [7,1,5,3,6,4]
print(max_profit(arr))


