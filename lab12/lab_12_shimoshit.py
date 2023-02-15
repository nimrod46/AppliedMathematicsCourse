"""
Created on Sat Jan 28 18:33:59 2023
@Credit to: @RotemLevi1
"""

import pandas as pd
import numpy as np

rain_df = pd.read_csv('data_full.csv')
rain_df['Measurement'].shape
rain_df['Measurement'].values
rain_df['Measurement'].mean()
# rain_df['Measurement'].hist()
# plt.show()
rain_df.iloc[20:50, 2:5]
rain_df['Measurement'] == 0
(rain_df['Measurement'] == 0).any()
# any returns true if only one is true
rain_df.loc[rain_df['Measurement'] == 0, :]
rain_df.loc[np.logical_and(rain_df['Measurement'] > 0, rain_df['Year'] == 2015), 'Measurement'].sum()
rain_df.groupby('Month')['Measurement'].agg(['sum', 'mean'])
rain_df.loc[rain_df['Year'] == 2013, ['Measurement', 'DoY']]
l = list(rain_df.loc[rain_df['Year'] == 2013, 'Measurement'])
l = l + [0] * 10

d = rain_df.groupby('Month')['Measurement'].sum()
d.max
d.argmax()
d.argmin()  # will give the index of that place
d.index[d.argmin()]

d.loc[d > 9]
# d.loc[d>9].item()
# LAB EXPLENATIONS ON THE ABOVE

# Q3
print((rain_df.loc[rain_df['Year'] == 2000, 'Measurement'].sum()) / 365)
# Q4
l = list(rain_df.loc[rain_df['Year'] == 2000, 'Measurement']) + [0] * (365 - 80)
print(np.median(l))
# Q5
d = rain_df.groupby('Month')['Measurement'].mean()
print(d.index[d.argmax()])
# Q6
d = rain_df.loc[rain_df['Measurement'] > 0, :].groupby('Month')['Measurement'].count()
print(d.index[d.argmax()])
# Q7
d = rain_df.loc[rain_df['Measurement'] > 0, :].groupby('DoY')['Measurement'].count()
# v = d.loc[:, 'Measurement']
print(d.index[d.argmax()])
# Q8
d = rain_df.loc[np.logical_and(rain_df['Measurement'] > 0, rain_df['DoY'] == 28), 'Measurement'].median()
print(d)
# Q9
w = rain_df.loc[:, ['Measurement', 'DoY']]
v = w.loc[:, 'Measurement']
print(max(v))
# Q10
w = rain_df.groupby('Year')['Measurement'].max()
print(w.index[w.argmax()])
# Q11
v = rain_df.groupby('Year')['Measurement'].sum()
v = v.diff()
d = v.loc[v < 0]
print(d.count())
# Q12
v = rain_df.loc[rain_df['Measurement'] > 0, :].groupby('Year')['Measurement'].count()
d = v.diff()
d = d.loc[d < 0]
print(d.count())
