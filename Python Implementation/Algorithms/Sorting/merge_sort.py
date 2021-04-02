def mergeSort(arr):
    mid = len(arr)//2
    L_arr = arr[:mid] #L_arr does not include middle element
    R_arr = arr[mid:] 

    # base case
    if len(arr) == 1:
        return
    
    # sort the two halves
    mergeSort(L_arr)
    mergeSort(R_arr)

    # merge sorted arrays
    i = j = k = 0
    while i < len(L_arr) and j < len(R_arr):
        if L_arr[i] < R_arr[j]:
            arr[k] = L_arr[i]
            i += 1
        else:
            arr[k] = R_arr[j]
            j +=1 
        k += 1

    # add remaing elements from a array (only one while loop will be executed)
    while i < len(L_arr):
        arr[k] = L_arr[i]
        i += 1
        k += 1
    while j < len(R_arr):
        arr[k] = R_arr[j]
        j += 1
        k += 1


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    mergeSort(arr)
    print(arr)