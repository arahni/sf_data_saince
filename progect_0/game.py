"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min_int = 1 # минимальное угадыаемое число
    max_int = 100 # максимальное угадываемое число

    while True:
        count += 1
        predict_number = (min_int + max_int) // 2 # предполагаемое число

        if(predict_number < number): 
            min_int = predict_number + 1 # увеличиваем минимальное 

        elif(predict_number > number):
            max_int = predict_number - 1 # уменьшаем максимальное

        else:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict, switch_seed=True) -> int:
    """_summary_

    Args:
        random_predict (_type_): функция угадывания
        switch_seed (bool, optional): Включение воспроизводимости случайных чисел. По умолчанию True.

    Returns:
        int: среднее количество попыток
    """
    count_ls = []

    if switch_seed:
        np.random.seed(1)  # фиксируем сид для воспроизводимости

    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    print("seed выключен")
    score_game(random_predict, False)
    print("seed включен")
    score_game(random_predict)
    