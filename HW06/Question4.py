import pandas as pd
from matplotlib import pyplot as plt

from HW06.Question3 import get_mean, get_variance, get_standard_deviation, get_coefficient_of_variation, get_median, \
    get_interquartile_range

df = pd.read_csv('education_Data.csv', na_values=":", usecols=["TIME", "GEO",
                                                                "Value"])
country_list = ['Ireland', 'Germany', 'Estonia', 'Czech Republic', 'Denmark', 'Belgium', 'Bulgaria',
                'Latvia', 'Lithuania', 'Luxembourg', 'Hungary', 'Greece', 'Spain', 'France', 'Italy', 'Cyprus',
                'Slovakia', 'Netherlands', 'Austria', 'Poland', 'Portugal', 'Romania', 'Malta', 'Finland']

for country in country_list:
    mean = get_mean(df[df.GEO.str.contains(country, case=False)].Value)
    var = get_variance(df[df.GEO.str.contains(country, case=False)].Value)
    standard_dev = get_standard_deviation(df[df.GEO.str.contains(country, case=False)].Value)
    coe_var = get_coefficient_of_variation(df[df.GEO.str.contains(country, case=False)].Value)
    med = get_median(df[df.GEO.str.contains(country, case=False)].Value)
    iqr = get_interquartile_range(df[df.GEO.str.contains(country, case=False)].Value)

