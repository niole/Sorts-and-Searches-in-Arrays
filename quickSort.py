import random
"""
Recursively sorts sections of an unsorted array
around a designated partition element and returns
a sorted list.
"""
def quickSort(l):
    if len(l) == 0:
        return l
        # do something
    else:
        partition = l[0]
        lowPart = [l[i] for i in range(len(l)) if l[i] < partition]# stuff < partition
        partitionRep = [l[i] for i in range(len(l)) if l[i] == partition]# stuff == partition
        highPart = [l[i] for i in range(len(l)) if l[i] > partition]# stuff > partition
        return quickSort(lowPart) + partitionRep + quickSort(highPart)

L = [2,8,5,0,7,8,1]
print quickSort(L)
