def swap(arr,a,b):
    temp = arr[a]
    arr[a]=arr[b]
    arr[b]=temp
def partition(arr,start,end):
    pivot = arr[end]
    pindex = start
    for i in range(start,end):
        if arr[i] <= pivot:
            swap(arr,i,pindex)
            pindex = pindex + 1
    swap(arr,end,pindex)
    return pindex
            
def quicksort(arr,start,end):
    if (start < end):
        pindex = partition(arr,start,end)
        quicksort(arr,pindex+1,end)
        quicksort(arr,start,pindex-1)


arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
quicksort(arr,0,9)
print(arr)