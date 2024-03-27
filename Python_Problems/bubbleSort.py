arr1 = [1,3,5,6,3,2,4,0]
arr2 = [0,1,2,3,4,5,6,7]
arr3 = [7,6,5,4,3,2,1,0]

def bubbleSort(arr):
    max = len(arr) - 1
    # backstop for the last element that is sorted
    while max > 0:
        count = 0
        # sort from start of array to last element sorted
        while count < max:
            # flip element if left is lower
            if arr[count] > arr[count + 1]:
                temp = arr[count]
                arr[count] = arr[count + 1]
                arr[count + 1] = temp
            count += 1
        max -= 1
    return arr

print(bubbleSort(arr1))
print(bubbleSort(arr2))
print(bubbleSort(arr3))
