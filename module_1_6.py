# Словари и множества
print('Практическая работа по теме "Словари и множества"')
# Создание словаря
print()
print()
print('Создаём словарь "my_dict"')
my_dict={'Евгений':1971,'Светлана':1973,'Константин':1983,'Елена':1984}
print('Вывод словаря "my_dict"')
print(my_dict)
print()
print('Вывод года рождения по ключу"Елена"')
print(my_dict['Елена'])
print()
print("Вывод не существующего элемента 'Антон'")
print(my_dict.get('Антон','Такого элемента нет'))
print()
print('Добавление элементов в словарь')
my_dict.update({'Антон':1996,
                'Артур':1996})
print(my_dict)
print()
print('Вывод удаленого элемента "Елена" на панель')
print(my_dict.pop('Елена'))
print('Вывод словаря "my_dict"')
print(my_dict)
print()
print()
print()
# Работа со мноюествами
print('Работа со мноюествами')
print("Создаем множество - 1,2,3,2,4,6,6,4,3,2,'a','d','h','a','h','d','f'")
my_set = {1,2,3,2,4,6,6,4,3,2,'a','d','h','a','h','d','f'}
print(my_set)
print()
my_set.update({'g',5})
print("Добавили элементы -'g',5")
print(my_set)
print()
print("Удалили элемент 1")
#
a=my_set.remove(1)
print(my_set)
print()
print()
print("Задание выполнено")
