"""
Возьмите 10 любых файлов формата csv, прочитайте их в
разные переменные с помощью библиотеки Pandas,
сохраните их в один файл формата hdf5; прочитайте одну
любую таблицу из сохраненного файла hdf5
"""
import pandas as pd

for i in range(1,11):
    df = pd.read_csv(f'data08_{i}.csv')
    df.to_hdf('data8.h5', f'df_{i}')



df = pd.read_hdf('data8.h5', 'df_4')
print(df)