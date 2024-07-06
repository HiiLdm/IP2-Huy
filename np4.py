import numpy as np

a = np.array([2, 6, 1, 9, 10, 3, 27])

# Lọc ra các phần tử trong khoảng từ 5 đến 10
result = a[(a >= 5) & (a <= 10)]

print("Các phần tử trong khoảng từ 5 đến 10:")
print(result)
