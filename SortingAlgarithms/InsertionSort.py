def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step -1       
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


data = [10, -20, 15,-12,82,0]
print('UnSorted Array in Ascending Order:',data)
insertionSort(data)
print('Sorted Array in Ascending Order:',data)
