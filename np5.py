import numpy as np

arr = np.arange(9).reshape(3, 3)
print("Original array:")
print(arr)

# Swap column 0 with column 1
arr[:, [0, 1]] = arr[:, [1, 0]]

print("\nArray after swapping column 0 with column 1:")
print(arr)
