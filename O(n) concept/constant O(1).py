# Constant Time: O(1)
# The operation's time does not depend on the input size.
# Example: Accessing an element in an array by index.

def get_first_element(arr):
    return arr[0]  # Always takes the same time regardless of array size.

print(get_first_element([11,24,36,48,51,63]))