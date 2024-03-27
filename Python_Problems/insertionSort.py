arr1 = [1,3,5,6,3,2,4,0]
arr2 = [0,1,2,3,4,5,6,7]
arr3 = [7,6,5,4,3,2,1,0]

def insertionSort(arr):
    if len(arr) == 1:
        return arr

    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1

        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = temp

    return arr

print(insertionSort(arr1))
print(insertionSort(arr2))
print(insertionSort(arr3))