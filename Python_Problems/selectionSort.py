arr1 = [1,3,5,6,3,2,4,0]
arr2 = [0,1,2,3,4,5,6,7]
arr3 = [7,6,5,4,3,2,1,0]

def selectionSort(arr):
    start = 0
    # iterate through the array skipping min sorted values
    while start < len(arr):
        count, minIndex = start, start
        # iterate through to find the min
        while count < len(arr):
            if arr[count] < arr[minIndex]:
                minIndex = count
            count += 1
        # swap the min with the next unsorted slot
        temp = arr[start]
        arr[start] = arr[minIndex]
        arr[minIndex] = temp
        start += 1

    return arr

print(selectionSort(arr1))
print(selectionSort(arr2))
print(selectionSort(arr3))