def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_index = i
        # j pointer starts at i - 1
        j = i - 1

        while j >= 0 and arr[j+1] < arr[j]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            j -= 1
        print(arr)
    



    return arr

if __name__ == "__main__":
    x = [5, 2, 9,3, 1, 6]
    print(insertion_sort(x))