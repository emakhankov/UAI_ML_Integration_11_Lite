"""
Напишите класс/функцию на языке Python и сохраните
полученный результат в pickle формат. Прочитайте
сохраненную функцию в новую переменную с помощью
билиотеки pickle
"""
import pickle


class House:
    rooms = 0

    def add_room(self):
        self.rooms += 1


# Класс в питоне это тоде объект
print(type(House))

with open('data06.pickle', 'wb') as f:
    pickle.dump(House, f)

with open('data06.pickle', 'rb') as pickle_file:
    pickle_object = pickle.load(pickle_file)

print(type(pickle_object))
print(pickle_object)

ob = pickle_object()

print(type(ob))
print(ob)
