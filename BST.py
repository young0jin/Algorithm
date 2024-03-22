#Binary Search Tree

#How 1 
#By using iteration

def BSTiteration(arr, target):
    arr = []
    low = 0
    high = len(arr) - 1
    
    while low <= high :
        mid = (low + high) / 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid -1
        else:
            low = mid + 1

    return -1


#By using Recursive
def BSTrecursive(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) / 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target :
        return BSTrecursive(arr, target, low, mid - 1)
    else:
        return BSTrecursive(arr, target, mid + 1, high)
    
