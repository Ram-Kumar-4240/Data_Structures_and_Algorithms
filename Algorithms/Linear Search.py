def linear_search(arr, target):
    for i in range(len((arr))):
        if arr[i] == target:
            return       
    return -1
arr = [25,79,53,65,97]
target = 65
print(linear_search(arr,target))
