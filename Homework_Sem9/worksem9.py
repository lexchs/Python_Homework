# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

# Узнать какая максимальная households в зоне минимального значения population.
import pandas as pd


df = pd.read_csv('california_housing_test.csv')

# ndf = df[df['population'] < 501]
# print(ndf['median_house_value'].mean())


# print(df.loc[df['population'] == (df['population'].min()), ['population', 'households']])


