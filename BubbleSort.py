def bubbleSort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return (arr)

myList = [12,76,13,98,34,62,100]
myList = bubbleSort(myList)
print(myList)

