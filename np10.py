import pandas as pd
import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"


df = pd.read_csv(url, header=None, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'class'])


random_rows = np.random.choice(df.index, size=10, replace=False)
random_cols = np.random.choice(df.columns, size=2, replace=False)

df.loc[random_rows, random_cols] = np.nan


df = df.fillna(0)
print(df.head(10))
