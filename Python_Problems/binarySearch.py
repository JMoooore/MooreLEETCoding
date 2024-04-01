arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# find index of given value
def binarySearch(arr, k):
    def binarySearchHelper(arr, k, l, r):
        mid = (l + r) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] != k and l == r:
            return -1
        elif arr[mid] > k:
            return binarySearchHelper(arr, k, l, mid-1)
        elif arr[mid] < k:
            return binarySearchHelper(arr, k, mid+1, r)

    return binarySearchHelper(arr, k, 0, len(arr)-1)

print(binarySearch(arr1, 0))
