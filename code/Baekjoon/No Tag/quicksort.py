import random

def quicksort(arr:list):
    def __sort(low:int, high:int):
        if (high > low):
            pivotpoint = partition(low,high)
            __sort(low,pivotpoint-1)
            __sort(pivotpoint+1,high)

    def partition(low:int,high:int)->int:
        # choose the first time for pivotitem
        pivotpoint = low
        pivotitem = arr[low]
        for i in range(low+1,high+1):
            if arr[i] < pivotitem:
                pivotpoint += 1
                arr[i], arr[pivotpoint] = arr[pivotpoint], arr[i]
        arr[pivotpoint], arr[low] = arr[low], arr[pivotpoint]
        return pivotpoint
    return __sort(0,len(arr)-1)

test_list = [i for i in range(10)]
random.shuffle(test_list)
print("not_sorted:",test_list)
quicksort(test_list)
print("sorted",test_list)