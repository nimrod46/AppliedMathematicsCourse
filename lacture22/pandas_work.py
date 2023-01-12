from matplotlib.pyplot import plot

import pandas as pd
import numpy as np

river_lengths = pd.Series([6300, 6650, 6275, 6400])

river_lengths = pd.Series([6300, 6650,
                           6275, 6400], name='Length /km',
                          dtype=float)

river_lengths = pd.Series([6300, 6650,
                           6275, 6400], name='Length /km',
                          dtype=float)
river_lengths = pd.Series([6300, 6650,
                           6275, 6400], index=['Yangtze', 'Nile', 'mississippi', 'Amazon'], name='Length /km',
                          dtype=float)

river_lengths[1]
river_lengths['Nile']
river_lengths[1:3]
river_lengths['Nile':'Amazon']
river_lengths[river_lengths <= 6600]

edu = pd.read_csv('education_Data.csv', na_values = ":", usecols=["TIME", "GEO",
                                                                  "Value"])

edu.head(10)
edu.tail(15)
edu.describe()
