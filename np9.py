import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Đọc dữ liệu vào DataFrame của pandas
df = pd.read_csv(url, header=None, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'class'])

# Lọc các dòng thỏa mãn điều kiện
filtered_data = df[(df['petallength'] > 1.5) & (df['sepallength'] < 5.0)]

# In ra màn hình các dòng đã lọc
print(filtered_data)
