def binarySearch(arr, num):
    left_index = 0
    right_index = len(arr) - 1
    middle_index = (left_index + right_index) // 2

    if arr[middle_index] == num:
        # found num index
        return middle_index
    elif arr[middle_index] < num:
        # search right half of the array
        pass
    else:
        pass
        # search the left half of the array


def main(): 
    # ordered list  
    sample = [4, 8, 12, 20, 22, 35, 45, 57, 62, 78, 84, 91]
    binarySearch(sample, 63)

if __name__ == "__main__"

        
    print("Hello")