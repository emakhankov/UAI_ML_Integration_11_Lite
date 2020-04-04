"""
Добавьте данные в созданный файл с помощью методов
append и write
"""

print('Исходный файл')
with open('data02.txt', 'r') as f:

    line = f.readline()
    cnt = 1
    while line:
        print(line.strip())
        line = f.readline()
        cnt += 1


with open('data02.txt', 'a') as f:

    f.write('А это новые данные')

print('-'*10)
print('Файл после добавления append')
print('-'*10)
with open('data02.txt', 'r') as f:
    line = f.readline()
    cnt = 1
    while line:
        print(line.strip())
        line = f.readline()
        cnt += 1


with open('data02.txt', 'w') as f:

    f.write('А это новые данные')

print('-'*10)
print('Файл после добавления write')
print('-'*10)

with open('data02.txt', 'r') as f:
    line = f.readline()
    cnt = 1
    while line:
        print(line.strip())
        line = f.readline()
        cnt += 1