def linear(A,n,key):
    index = 0
    while index < n:
        if A[index] == key:
            return index
        index += 1
    return -1

A = [84,21,47,96,15]
n = len(A)
key = 96

print(linear(A,n,key))
