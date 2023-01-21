import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from HW06.Question3 import get_mean, get_variance, get_standard_deviation, get_coefficient_of_variation, get_median, \
    get_interquartile_range

df = pd.read_csv('education_Data.csv', na_values=":", usecols=["TIME", "GEO",
                                                               "Value"]).dropna()

country_list = ['Ireland', 'Germany', 'Estonia', 'Czech Republic', 'Denmark', 'Belgium', 'Bulgaria',
                'Latvia', 'Lithuania', 'Luxembourg', 'Hungary', 'Greece', 'Spain', 'France', 'Italy', 'Cyprus',
                'Slovakia', 'Netherlands', 'Austria', 'Poland', 'Portugal', 'Romania', 'Malta', 'Finland']

# a:
means = np.zeros(len(country_list))
standard_devs = np.zeros(len(country_list))
medians = np.zeros(len(country_list))
for i, country in enumerate(country_list):
    c_df = df[df.GEO.str.contains(country, case=False)].Value
    mean = get_mean(c_df)
    var = get_variance(c_df)
    standard_dev = get_standard_deviation(c_df)
    coe_var = get_coefficient_of_variation(c_df)
    med = get_median(c_df)
    iqr = get_interquartile_range(c_df)

    means[i] = mean
    standard_devs[i] = standard_dev
    medians[i] = med

# b:
fig, ax = plt.subplots(2, figsize=(10, 9))
ax[0].barh(country_list, means, xerr=standard_devs, label='mean')
ax[0].legend()

# c:
ax[1].barh(country_list, medians, label='median')
ax[1].legend()

plt.show()
