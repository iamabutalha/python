


from typing import final


def checkMid(arr):
    if len(arr) % 2 == 1:

        length = int(len(arr)/2)
        mid = arr[length]

        return mid
    
    elif len(arr) % 2 == 0:
        length1 = int(len(arr)/2)
        mid1 = length1
        mid2 = length1 + 1

        finalmid = mid1 + mid2
        return finalmid 


print(checkMid([1,2,3,4,5,90,8,9])) #→ 9
print(checkMid([3,4,5,90,8,9,8,5])) #→ Some issues here
print(checkMid([1,2,3,4,])) #→ 5
print(checkMid([1,2,3,2])) #→ 5