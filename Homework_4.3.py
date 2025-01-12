# Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.
# Ваше завдання - створити новий список з 3 елементів початкового списку - першим, третім і другим з кінця.
# Приклад:
# [1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
# [1, 1, 2, 1] == [1, 2, 2]
# [6, 3, 7] == [6, 7, 3]
import random


def create_random_list():
    length_of_thr_list = random.randint(3, 10)
    return [random.randint(1, 100) for _ in range(length_of_thr_list)]


def select_elements_from_the_list(incoming_list):
    try:
        if len(incoming_list) < 3:
            raise ValueError("The list should not be empty and should contain 3 or more elements")

        selected_list = [incoming_list[0], incoming_list[2], incoming_list[-2]]
        return selected_list

    except ValueError as exception:
        return str(exception)


random_list = create_random_list()

print(f"Generated list: {random_list}")
print(f"Result: {select_elements_from_the_list(random_list)}")
print("-" * 40)
