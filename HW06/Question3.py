import numpy as np

import pandas as pd


def get_mean(x):
    return np.sum(x) / np.size(x)


def get_variance(x):
    return np.sum((x - get_mean(x)) ** 2) / (np.size(x) - 1)


def get_standard_deviation(x):
    return get_variance(x) ** 0.5


def get_coefficient_of_variation(x):
    return get_standard_deviation(x) / get_mean(x)


def get_median(x):
    n = np.size(x)
    x_c = np.sort(x)
    if n % 2 == 1:
        return x_c[(n + 1) // 2 - 1]
    return get_mean([x_c[n // 2 - 1], x_c[n // 2]])


def get_interquartile_range(x):
    n = np.size(x)
    x_c = np.sort(x)
    return get_median(x_c[(n - 1) // 2: n]) - get_median(x_c[: (n - 1) // 2 + 1])

def test():
    df_even = pd.Series([3, 5, 7, 8, 9, 11, 15, 16, 20, 21])
    df_odd = pd.Series([19, 2, 18, 9, 27, 6, 12, 15, 5, 1, 7])

    assert df_even.mean() == get_mean(df_even)
    assert df_odd.mean() == get_mean(df_odd)

    assert df_even.var() == get_variance(df_even)
    assert df_odd.var() == get_variance(df_odd)

    assert df_even.std() == get_standard_deviation(df_even)
    assert df_odd.std() == get_standard_deviation(df_odd)

    assert df_even.std() / df_even.mean() == get_coefficient_of_variation(df_even)
    assert df_odd.std() / df_odd.mean() == get_coefficient_of_variation(df_odd)

    assert df_even.median() == get_median(df_even)
    assert df_odd.median() == get_median(df_odd)

    Q3 = np.quantile(df_even, 0.75)
    Q1 = np.quantile(df_even, 0.25)
    IQR = Q3 - Q1
    assert IQR == get_interquartile_range(df_even)

    Q3 = np.quantile(df_odd, 0.75)
    Q1 = np.quantile(df_odd, 0.25)
    IQR = Q3 - Q1
    assert IQR == get_interquartile_range(df_odd)

if __name__ == '__main__':
    test()
