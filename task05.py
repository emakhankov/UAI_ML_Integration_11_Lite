"""
Найдите любой файл формата csv, прочитайте его с помощью
библиотеки Pandas и сохраните полученный результат в
формат pickle, прочитайте pickle файл с помощью библиотеки
pickle и с помощью библиотеки Pandas
"""
import pandas as pd
import pickle

df = pd.read_csv('data05.csv')
df.to_pickle('data05.pickle')


with open('data05.pickle', 'rb') as pickle_file:
    pickle_object = pickle.load(pickle_file)

print(type(pickle_object))
print(pickle_object)
print('-'*10)

df2 = pd.read_pickle('data05.pickle')
print(df2)