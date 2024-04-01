arr1 = [0,3,5,6,3,2,4,1]
arr2 = [0,1,2,3,4,5,6,7]
arr3 = [7,6,5,4,3,2,1,0]

# quicksort is supposed to sort in place
def quickSort(arr):

    def qsort (arr, l, r):
        if l >= r:
            return arr

        pivot = arr[r]

        i,j = l,l
        while j < r:
            # If right pointer is less swap them and move both forward
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1
            # if right pointer is greater or equal push right pointer forward
            else:
                j += 1
        # swap the pivot with the left item since we know itll be in the middle
        arr[i], arr[j] = arr[j], arr[i]

        qsort(arr, l, i-1)
        qsort(arr, i+1, r)

        return arr

    return qsort(arr, 0, len(arr)-1)

print(quickSort(arr1))
print(quickSort(arr2))
print(quickSort(arr3))