                                                   ###ЯДРО ИГРЫ###

from random import randint

def progression():
    ###Создаем алгеброическу прогрессию 
    d = randint(0, 10)
    a = randint(0, 100)
    result = []
    result.append(a) # записываем первый симвло
    i = 0
    while i < 10:     
        new_row = result[i] + d #создаем временную переменную
        result.append(new_row) # записываем элементы прогресии
        i += 1  
    return result #возвращаем строку-прогрессию

def progression_string():
    ### Создаем строку алгеброической прогресии с неизвестным элементом
    temporary_list = list(map(str, progression()))  # Преобразуем строку в список
    ind = randint(1, len(temporary_list) - 1)
    temporary_list[ind] = '..'
    temporary_string = ' '.join(temporary_list)  # Преобразуем список обратно в строку
    print(f'Question: {temporary_string}')
    return ind  # Возвращаем индекс



