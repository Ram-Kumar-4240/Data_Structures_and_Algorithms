# Cubic Time: O(n³)
# The operation time increases cubically with the input size.
# Example: Matrix multiplication or three nested loops.

def cubic_operation(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(arr[i], arr[j], arr[k])  # Example of cubic complexity.
