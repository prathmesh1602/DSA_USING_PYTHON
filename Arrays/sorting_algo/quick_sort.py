def quicksort(arr,left,right):

    if left<right:
        partition_pos = partition(arr,left,right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr,partition_pos + 1,right)


def partition(arr,left,right): 
    i = left - 1
    pivot = arr[right]

    for j in range(left,right):
        if arr[j] <= pivot:
            i =i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[right] = arr[right],arr[i+1]
    return i+1        

    

arr =[5,8,1,2,2,6,3,9,9,10]
quicksort(arr,0,len(arr)-1)
print(arr)           
