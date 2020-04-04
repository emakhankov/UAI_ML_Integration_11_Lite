"""
Найдите любой файл формата csv, прочитайте его с помощью
библиотеки Pandas
"""

import pandas as pd

df = pd.read_csv('data04.csv')

print(df.head())