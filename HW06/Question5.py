import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from HW06.Question3 import get_mean, get_variance, get_standard_deviation, get_coefficient_of_variation, get_median, \
    get_interquartile_range

df = pd.read_csv('adult.csv', na_values=":", usecols=["hr_per_week", "sex",
                                                      "age", 'income']).dropna()
bar_names = ['mean', 'standard deviation', 'coefficient_of_variation', 'median', 'interquartile range']

m_df = df[df.sex.str.contains('male', case=False)].hr_per_week
m_mean = get_mean(m_df)
m_var = get_variance(m_df)
m_standard_dev = get_standard_deviation(m_df)
m_coe_var = get_coefficient_of_variation(m_df)
m_med = get_median(m_df)
m_iqr = get_interquartile_range(m_df)

f_df = df[df.sex.str.contains('female', case=False)].hr_per_week
f_mean = get_mean(f_df)
f_var = get_variance(f_df)
f_standard_dev = get_standard_deviation(f_df)
f_coe_var = get_coefficient_of_variation(f_df)
f_med = get_median(f_df)
f_iqr = get_interquartile_range(f_df)

fig, ax = plt.subplots(figsize=(10, 9))

ax.hist([m_df, m_mean, m_standard_dev, m_coe_var, m_med, m_iqr], label='Male')
ax.hist([f_df, f_mean, f_standard_dev, f_coe_var, f_med, f_iqr], label='Female')
ax.legend()
plt.show()