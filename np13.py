import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"


df = pd.read_csv(url, header=None, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'class'])


value_counts = df['petallength'].value_counts()


max_count = value_counts.max()
most_repeated_value = value_counts.idxmax()


print(f"{max_count}, {most_repeated_value:.2f}")
