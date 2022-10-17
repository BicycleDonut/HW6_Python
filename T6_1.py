# 1. Представлен список чисел. Необходимо вывести элементы
#    исходного списка, значения которых больше предыдущего элемента.
#    Use comprehension.

from random import sample


def more_then_pre(num):
    original_list = sample(range(num * 3), num)
    print(original_list)
    return [original_list[num] for num in range(1, len(original_list)) if original_list[num] > original_list[num - 1]]


print(more_then_pre(int(input())))


