#NOT WORKING
countQuick = 0
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,start,end):
    if start < end:
        splitpoint = partition(alist,start,end)

        quickSortHelper(alist,start,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,end)

def partition(alist,start,end):
    pivotvalue = alist[start]
    leftmark = start+1
    rightmark = end

    done = False
    while not done:
        while leftmark<=rightmark and alist[leftmark] <= pivotvalue:
            leftmark+=1
        while rightmark>=leftmark and alist[rightmark] >= pivotvalue:
            rightmark-=1

        if rightmark < leftmark:
            done = True
        else:
            countQuick+=1
            alist[rightmark], alist[leftmark] = alist[leftmark], alist[rightmark]

    countQuick+=1
    alist[rightmark],alist[start] = alist[start], alist[rightmark]

    return rightmark

def insertionSort(list):
    n = len(list)
    count = 0
    for i in range(1,n):
        cur = list[i]
        for j in range(i,0,-1):
            if list[j-1] < cur:
                break
            else:
                conut+=1
                list[j] = list[j-1]
        list[j] = cur

    return count

n = int(input())

L = [int(i) for i in input().split()]

print(quickSort(L))
print(countQuick)
print(insertionSort(L))
