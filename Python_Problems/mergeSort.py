arr1 = [1,3,5,6,3,2,4,0]
arr2 = [0,1,2,3,4,5,6,7]
arr3 = [7,6,5,4,3,2,1,0]
def merge(left, right):
    l,r = 0,0
    result = []

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result += left[l:]
    return result + right[r:]

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    return merge(mergeSort(left), mergeSort(right))

print(mergeSort(arr1))
print(mergeSort(arr2))
print(mergeSort(arr3))