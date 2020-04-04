"""
Найдите любой файл формата excel, содержащий несколько
листов, прочитайте его с помощью библиотеки Pandas
(прочитайте только определенный лист.)
"""

import pandas as pd

df = pd.read_excel('data07.xlsx','students', 0)

print(df)