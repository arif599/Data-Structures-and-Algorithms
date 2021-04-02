def partition(arr, start, end):
    pivotIndex = start
    pivot = arr[pivotIndex]

    while start < end:
        while(start < len(arr) and arr[start] < pivot):
            # ex: pivot = 29 and arr = 15 28, start will keep incrementing
            start += 1
        
        while(end >= 0 and arr[end] > pivot):
            end -= 1

        if start > end:
            # put pivot in the right position and exit
            temp = arr[end]
            arr[end] = arr[pivotIndex]
            arr[pivotIndex] = temp
            break

        # swap
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
    
    return end
    

def quickSort(arr, start, end):
    # base case
    if start > end:
        return 

    partitionIndex = partition(arr, start, end)
    quickSort(arr, start, partitionIndex-1) # left partition
    quickSort(arr, partitionIndex+1, end) # right partition

if __name__ == "__main__":
    arr = [28, 17, 45, 51]
    quickSort(arr, 0, len(arr)-1)
    print(arr)