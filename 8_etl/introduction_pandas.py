import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt 

ROOT_PATH = Path(__file__).parent
df = pd.read_csv(ROOT_PATH / "data" / "2025-12-17_raw.csv")
print(df.head(n=4)) # firts lines
print(df.shape) # (lines, columns)
print(df.info())
print(df.isnull().sum())
print(df['Produto'].unique()) # unique values in columns

df["Produto"].value_counts().plot(kind='bar')

plt.show()