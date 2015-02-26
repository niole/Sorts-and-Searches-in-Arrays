"""
Sorts and unordered list by moving each subsequent entry
up or down the list until it is greater than the previous
entry and smaller than the next entry and returns
sorted list.
"""
def shiftUp(l,i0,i1):
    cellUp = l[i0]
    cellDown = l[i1]
    l[i1] = cellUp
    l[i0] = cellDown
    return insertionSort(l,i0,i1)

def shiftDown(l,i0,i):
    cellDown = l[i0]
    cellUp = l[i]
    l[i0] = cellUp
    l[i] = cellDown
    return insertionSort(l,i,i0)

def insertionSort(l,i0,i1):
    if i1 == len(l):
        return l
    if i0 > 0 and l[i0] >= l[i0-1] and l[i0] < l[i1]:
        return insertionSort(l,i0+1,i1+1)
    if l[i0] < l[i1] and i0 == 0:
        return insertionSort(l,i0+1,i1+1)
    else:
        if l[i0] > l[i1]:
            return shiftUp(l,i0,i1)
        if l[i0] < l[i0-1]:
            return shiftDown(l,i0,i0-1)

L = [7,10,3,30,2,3]
print insertionSort(L,0,1)
