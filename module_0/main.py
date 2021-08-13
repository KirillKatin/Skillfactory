def greet():
    print(" -----------------------")
    print("  Определим количество  ")
    print("      попыток для      ")
    print("    угадывания числа  ")
    print(" в диапазоне от 1 до 100")
    print(" ----------------------- ")

greet()

import numpy as np

def game_core(number):
    '''Устанавливаем диапазон чисел для угадывания, берем среднне арифметическое и сравниваем с загаданным числом.'''
    range_from = 1                              # диапазон чисел, начиная от
    range_to = 100                              # диапазон чисел, заканчивая
    number = np.random.randint(range_from,range_to) # загадали число
    count = 0                                   # счетчик попыток

    while True:                                 # бесконечный цикл
        predict = (range_from + range_to) // 2  # среднее арифметическое при делении без остатка
        count += 1
        if predict == number:
            break                               # выход из цикла, если угадали
        elif predict < number:
            range_from = predict                # среднне арифметическое принимает значение начала диапазона чисел
        elif predict > number:
            range_to = predict                  # среднне арифметическое принимает значение конца диапазона чисел
    
    return(count)


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)                            # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим
    random_array = np.random.randint(1,101, size=(1000))
    
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    
    return(score)

score_game(game_core)
