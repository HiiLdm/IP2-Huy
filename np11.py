import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"


data = np.genfromtxt(url, delimiter=',', usecols=(2,), dtype=float)

categorical = []
for val in data:
    if val < 3:
        categorical.append('small')
    elif val >= 3 and val <= 5:
        categorical.append('medium')
    else:
        categorical.append('large')


print(categorical[:4])
