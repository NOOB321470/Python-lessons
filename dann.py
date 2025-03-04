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