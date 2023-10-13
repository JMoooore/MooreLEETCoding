/**
 * @param {number[]} arr
 * @return {number}
 */
 var peakIndexInMountainArray = function(arr) {
    for (let i=1; i<arr.length; i++) {
        if (arr[i-1]>arr[i]) {
            return i-1
        }
    }
};

//Worse but fun solution
const peakIndexInMountainArray = arr => arr.indexOf(Math.max(...arr))

//Binary Search Method (better but less fun)
const peakIndexInMountainArray = (A, low = 0, high = A.length - 1) => {
    if (!A.length) 
        return -1
    
    const mid = ((low + high) / 2) | 0
	
    if (A[mid] > A[mid - 1] && A[mid] > A[mid + 1])
        return mid
    
    if (A[mid] < A[mid - 1]) 
        return peakIndexInMountainArray(A, low, mid)
    
    if (A[mid] < A[mid + 1])
        return peakIndexInMountainArray(A, mid, high)
}