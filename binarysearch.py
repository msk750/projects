def binarysearch(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        elif mid>target:
            high=mid-1
    return -1
arr = [2, 4, 6]
target = 4
print(binarysearch(arr,target))
        