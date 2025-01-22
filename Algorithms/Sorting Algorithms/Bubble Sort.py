# This is a algorithm helps to sort a array
arr = [1,10,11,5,2]
while (True):
    a = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            a = False
            arr[i],arr[i+1] = arr[i+1],arr[i]
    if a == True:
        break
print(arr)
            