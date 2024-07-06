import numpy as np

np.random.seed(101)
arr = np.random.randint(1, 4, size=6)

# Tìm số lượng lớp có thể có trong mảng ban đầu
num_classes = np.max(arr)

# Tạo ma trận zero có kích thước (số lượng phần tử, số lượng lớp)
one_hot = np.zeros((arr.size, num_classes))

# Đặt các chỉ số tương ứng thành 1
one_hot[np.arange(arr.size), arr - 1] = 1

print(one_hot)
