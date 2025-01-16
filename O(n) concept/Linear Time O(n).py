# Linear Time: O(n)
# The operation time increases linearly with the size of the input.
# Example: Finding the maximum element in an array

def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val
