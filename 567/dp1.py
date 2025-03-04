import pandas as pd
df=pd.read_csv("boston.csv")
print(df.head())
print(df.tail())
df=df.fillna(0)
df=df.dropna()
print(df.info())
