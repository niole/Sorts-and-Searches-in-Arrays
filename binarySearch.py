"""
Recursively moves through a sorted list until the target
element is found and return target element.
"""
#finds element to use as comparision in sorted list
#[int] -> int
def splitL(l,target):
    if len(l)%2 == 1:
        i = (len(l)-1)/2
    else:
        i = len(l)/2
    return binSearch(l,l[i],i,target)

def binSearch(sortedL,compEl,i,target):
    if target not in sortedL:
        return "Target doesn't exist."
    if compEl == target:
        return 'You found '+str(target)+'.'
    else:
        if target > compEl:
            return splitL(sortedL[i:],target)
        if target < compEl:
            return splitL(sortedL[:i+1],target)

assert(binSearch([2,5,6,88,456],2,0,88) == 'You found 88.')
assert(binSearch([0,0,2],0,0,1) == "Target doesn't exist.")
assert(binSearch([-1,0,2,3,4,5],0,0,-2) == "Target doesn't exist.")
L = [1,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
print binSearch(L,L[0],0,5)
