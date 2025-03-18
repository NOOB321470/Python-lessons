my_list = []

my_list = list()

my_list = ['orange', 'banana', 'apple']
fruit = 'apple' in my_list
print(fruit)#оператор in возвращает Булев тип данных
my_list.reverse()#меняет местами элементы в списке

print(my_list)

reversed_list = reversed(my_list)# функция создает копию объекта с перевернутыми объектами внутри

print(list(reversed_list))

print(my_list)

my_list.sort(key=lambda x: x[-1])# key = lambda x задает ключ с помощью которого мы сможем отсортировать элементы в списке

print(my_list)

my_list.append('mango')#append добавляет объект в список

my_list.insert(0, 'cherry')#insert позволяет добавить объект в список по определённому индексу

my_list.remove('apple')#remove удаляет определённый оьъект в списке

my_list.pop(0)#принимает число если не принимает то удаляет последний объект в списке

my_list.clear()#полностью очищает все данные в списке 

new_list = [0] * 5 # генераторы списков создают связанные списки

print(new_list)

comp_list = [i for i in range(5)]# генераторы
print(comp_list)

double_list = [i * 2 for i in range(5)]# генераторы
print(double_list)

a = 1,# кортеж из одного типа данных

my_tuple = 'apple', 'banana', 'orange'
my_tuple = ('apple', 'banana', 'orange')
my_tuple = tuple('apple')
print(my_tuple)
my_tuple.count('p')# позволяет посчитать кол-во элементов в делимых объектах если такого элемента нет выдаёт ошибку
my_tuple.index('p')# определяет индекс элемента
my_tuple = (1, 2, 3, 4, 5, 6)
first, *rest, last = my_tuple# оператор * позволяет сохранить список лишних элементов ферст и ласт сохраняют первый и последний элементы
print(first)
print(rest)
print(last)
my_dict = {'key_1' : 1, 'key_2' : 2}# ключи всегда строки значение может быть любой тип данных
my_dict = dict(key_1 = 1, key_2 = 2)

value = my_dict['key_1']# получаем значение ключа

my_dict['new_key'] = 3# создаем новый ключ со значением

del my_dict['key_1']# удаляет значение и ключ

removed_value = my_dict.pop('key_2')# удаляет элемент по ключу возвращая его в вывод

last_value = my_dict.popitem()# удаляет и возвращает последнее ключ-значение ввиде кортежа
print(last_value)

my_dict = {'key_1' : 1, 'key_2' : 2}

for k in my_dict.keys():
    print(k)
for v in my_dict.values():
    print(v)
for k, v in my_dict.items():
    print(k, v)

my_list = [1, 2, 3]
other_list = my_list.copy()
other_list = list(my_list)


other_list[0] = 4
print(my_list[0])

my_dict = {'key_1' : 1, 'key_2' : 2}
other_dict = my_dict.copy()
other_dict = dict(my_dict)

other_dict['key_1'] = 4
print(my_dict['key_1'])

my_set = {1,1,2,2}# множества в них данные не повторяются неизменяемое множество
print(my_set)

unique = set('arnold schwarzenegger')
print(unique)

my_set = {1,2}

my_set.add(3)# добавляет данные в множества
print(my_set)

my_set = {1,2,3,4}

my_set.remove(3)# удаляет если нет элемента вызывает ошибку
print(my_set)

my_set.discard(3)# удаляет если нет элемента не вызывает ошибку
my_set.discard(2)
print(my_set)

evens = {2,8,10}
odds = {1,3,7}
primes = {2,3,5}

union = evens.union(odds)# объединение двух множеств
print(union)

intersection = evens.intersection(primes)# пересечение двух множеств
print(intersection)

my_string = 'Hello \'world\'\\'# обратный слэш комментит знаки форматируемой строки
print(my_string)

my_string = '       Hello    world         '

no_spaces = my_string.strip()# убираетпробелы в начале и конце строки
print(no_spaces)

to_list = my_string.split()# разделяет строку по заданному ему знаку 
print(to_list)


