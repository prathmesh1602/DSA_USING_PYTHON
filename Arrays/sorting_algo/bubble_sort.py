def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swappedd = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swappedd = True
        if not swappedd:
            break
        
arr = [1,6,5,4]
print(arr)
bubbleSort(arr)          
print(arr)