def insertnSort(arr):
    n = len(arr)
    for i in range(n):

        currEle = arr[i]

        while i>0 and currEle < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            currEle = arr[i]
    return(arr)

newList = [13,76,32,89,12]
insertnSort(newList)
print(newList)