"""
Создайте .txt файл, прочитайте файл с помощью Python
"""

with open('data01.txt', 'r') as f:

    line = f.readline()
    cnt = 1
    while line:
        print(line.strip())
        line = f.readline()
        cnt += 1

print()

with open('data01.txt', 'r') as f:

    line = f.readline()
    cnt = 1
    while line:
        print(line, end='')
        line = f.readline()
        cnt += 1