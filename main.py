string = input("Введите строку: ") # Запрашиваем у пользователя ввод строки
index = 0 # Инициализируем переменную, которая будет хранить индекс текущего символа
for char in string: # Цикл для перебора каждого символа в строке
    if char == 'е': # Проверяем, является ли текущий символ буквой 'e'
        print(f"Буква 'е' найдена на индексе: {index}") # Если да, то выводим его индекс
    index += 1 # Увеличиваем индекс на 1, чтобы перейти к следующему символу
