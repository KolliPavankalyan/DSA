def binarySearch(Arr,n,k):
    left = 0
    right  = n-1
    while left <= right:
        median = (left+right)//2
        if Arr[median]==k:
            return median
        elif  k < Arr[median]:
            right = median-1
        elif k > Arr[median]:
            left = median+1
    return -1

Arr = [1,30,52,76,98]
n = len(Arr)
k = 98
print(binarySearch(Arr,n,k))