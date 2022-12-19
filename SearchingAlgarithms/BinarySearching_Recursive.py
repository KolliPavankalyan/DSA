def BinaryRecursive(A,key,L,R):
    if L > R:
        return -1
    else:
        mid = (L+R)//2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return BinaryRecursive(A,key,L,mid-1)
        elif key > A[mid]:
             return BinaryRecursive(A,key,mid+1,R)

A = [15,21,47,84,96]
key = 84
L= 0
R = len(A)-1
print(BinaryRecursive(A,key,L,R))