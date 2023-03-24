import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from HW06.Question3 import get_mean, get_variance, get_standard_deviation, get_coefficient_of_variation, get_median, \
    get_interquartile_range



def analize(m_df, f_df, title):
    m_mean = get_mean(m_df)
    m_var = get_variance(m_df)
    m_standard_dev = get_standard_deviation(m_df)
    m_coe_var = get_coefficient_of_variation(m_df)
    m_med = get_median(m_df)
    m_iqr = get_interquartile_range(m_df)

    f_mean = get_mean(f_df)
    f_var = get_variance(f_df)
    f_standard_dev = get_standard_deviation(f_df)
    f_coe_var = get_coefficient_of_variation(f_df)
    f_med = get_median(f_df)
    f_iqr = get_interquartile_range(f_df)

    fig, ax = plt.subplots(1, 3, figsize=(16, 9))

    print('-----------' + str(title) + '----------')
    print('Male:')
    print('Mean:' + str(m_mean))
    print('Standard Dev:' + str(m_standard_dev))
    print('Median:' + str(m_med))
    print('IQR:' + str(m_iqr))
    print('---------------------')
    print('Female:')
    print('Mean:' + str(f_mean))
    print('Standard Dev:' + str(f_standard_dev))
    print('Median:' + str(f_med))
    print('IQR:' + str(f_iqr))
    print('---------------------')

    ax[0].hist([m_df, f_df], bins=20, label=['Male', 'Female'])
    ax[0].set_title("Hours per week")
    ax[1].hist([m_df, f_df], bins=20, density=True, label=['Male', 'Female'])
    ax[1].set_title("Normalized Hours per week")
    ax[2].hist([m_df, f_df], bins=20, cumulative=True, density=True, label=['Male', 'Female'])
    ax[2].set_title("Cumulative Hours per week")
    ax[0].legend()
    ax[1].legend()
    ax[2].legend()
    fig.suptitle(title)
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('adult.csv', na_values=":", usecols=["hr_per_week", "sex",
                                                          "age", 'income']).dropna()

    bar_names = ['mean', 'standard deviation', 'coefficient_of_variation', 'median', 'interquartile range']
    m_df = df[df.sex.str.fullmatch('male', case=False)].hr_per_week
    f_df = df[df.sex.str.fullmatch('female', case=False)].hr_per_week
    analize(m_df, f_df, 'Not filtered HPW')

    m_df_filtered = df[df.sex.str.fullmatch('male', case=False) &
                       df.income.str.contains('>50K', case=False)].hr_per_week
    f_df_filtered = df[df.sex.str.fullmatch('female', case=False) &
                       df.income.str.contains('>50K', case=False)].hr_per_week
    analize(m_df_filtered, f_df_filtered, 'High income HPW')

    df2 = df.drop(df.index[(df.hr_per_week > df.hr_per_week.median() + 25) |
                           (df.hr_per_week < df.hr_per_week.median() - 25)])

    print("dropped: " + str(df.shape[0] - df2.shape[0]))

    m_df = df2[df2.sex.str.fullmatch('male', case=False)].hr_per_week
    f_df = df2[df2.sex.str.fullmatch('female', case=False)].hr_per_week
    analize(m_df, f_df, 'Not filtered without outliers HPW')

    m_df_filtered = df2[(df2.sex.str.fullmatch('male', case=False)) &
                        (df2.income.str.contains('>50K', case=False))].hr_per_week
    f_df_filtered = df2[(df2.sex.str.fullmatch('female', case=False)) &
                        (df2.income.str.contains('>50K', case=False))].hr_per_week
    analize(m_df_filtered, f_df_filtered, 'High income without outliers HPW')
