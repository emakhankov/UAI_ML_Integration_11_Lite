"""
Найдите любой файл формата json, прочитайте его с помощью
библиотеки json и с помощью Pandas read_json
"""
import json
import pandas as pd


with open('data03.json', 'r') as f:
    js = json.load(f)
print(type(js))
print(js)
print('-'*10)
df = pd.read_json('data03.json')
print(df.head())

