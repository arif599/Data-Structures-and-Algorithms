def selection_sort(arr):
    for i in range(len(arr)):
        # initial min index is the element at i
        min_index = i
        new_min = False 
        for j in range(i+1, len(arr)):
            # look to see is there another number thats minimum compared to the default min
            if arr[min_index] > arr [j]:
                min_index = j
                new_min = True
        
        if new_min:
            # swap
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp
    return arr


if __name__ == "__main__":
    x = [64, 25, 12, 22, 11] 
    print(selection_sort(x))