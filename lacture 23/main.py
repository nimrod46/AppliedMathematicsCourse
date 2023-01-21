import numpy as np
import pandas as pd

df = pd.read_csv("adult.csv")
# print(df)
count = df.groupby('country').size()
# print(count)
fml = df[df.sex == 'Male']
ml = df[df.sex == 'Male']
mlh = df[(df.sex == 'Male') & (df.income == '>50K\n')]
# print(fml)
# print(ml)
print(mlh)

