import numpy as np
import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# read input
df = pd.read_csv(url, header=None, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'class'])

sepallength = df['sepallength'].values


mean_value = np.mean(sepallength)
median_value = np.median(sepallength)
std_deviation = np.std(sepallength)

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard deviation: {std_deviation}")
