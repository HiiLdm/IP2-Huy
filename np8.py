import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"


df = pd.read_csv(url, header=None, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'class'])


sepallength = df['sepallength']


min_val = sepallength.min()
max_val = sepallength.max()


df['sepallength_normalized'] = (sepallength - min_val) / (max_val - min_val)


print(df[['sepallength', 'sepallength_normalized']])
