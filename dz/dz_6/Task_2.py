import itertools
import random


def are_queens_attacking_each_other(queens_position):
    """
    Функция для проверки , атакует ли ферзи друг друга

    args:
    queens_position (list) список содержащий координаты ферзей по доске в формате ( строка, столбец )
    :returns
    bool: True усли ферзи не атакуют друг друга

    """
    for i in range(len(queens_position)):
        for j in range(i + 1, len(queens_position)):
            row1, col1 = queens_position[i]
            row2, col2 = queens_position[j]

            if row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2):
                return False
        return True


def generate_successful_arr():
    """
    Функция для генерации 4 успешных расстановок ферзей

    :return: List список с 4 успешными расстановками
    """

    successful_args = []
    all_permutation = list(itertools.permutations(range(1, 9)))
    random.shuffle(all_permutation)

    for permutation in all_permutation:
        queens_position = [(i + 1, permutation[i]) for i in range(8)]
        if are_queens_attacking_each_other(queens_position):
            successful_args.append(queens_position)
            if len(successful_args) == 4:
                break
    return successful_args


successful_arrangements = generate_successful_arr()

print("Успешные расстановки ферзей")
for i, arrangement in enumerate(successful_arrangements, 1):
    print((f"Расстановка {i}: {arrangement}"))
