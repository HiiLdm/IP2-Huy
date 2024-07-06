import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Đọc dữ liệu từ URL và lưu vào một numpy array
data = np.genfromtxt(url, delimiter=',', usecols=(0, 1, 2, 3))

print(data)
