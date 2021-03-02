def simple_bubble(arr):
    counter = 0

    for i in range(len(arr)):
        swap = False

        for j in range(len(arr)-i-1):
            counter += 1
            # j goes up to n-i because the last element will already be sorted
            # n-i-1 because j will be comparing the adjacent values so will get out of bounds without -1
            if arr[j] > arr[j+1]:
                # swap
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swap = True
        
        if swap == False:
            # if no swaps are made then the array is in order
            break
    
    print(counter)
    return arr

if __name__ == "__main__":
    x = [2, 7, 4, 1, 5, 3]
    print(simple_bubble(x))