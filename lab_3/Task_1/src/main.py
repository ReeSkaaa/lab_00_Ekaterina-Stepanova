import random
from ...utils import re

PATH = '../txtf/input.txt'
OUTPUT_PATH = '../txtf/output.txt'

def quick_sort(mas):
    if len(mas) <= 1:
        return mas
    elem = mas[random.randint(0, len(mas) - 1)]
    left = [i for i in mas if i < elem]
    mid = [elem] * mas.count(elem)
    right = [i for i in mas if i > elem]
    return quick_sort(left) + mid + quick_sort(right)


if __name__ == "__main__":
    data = read_f(PATH)
    n = int(data[0])
    mas = list(map(int, data[1].split()))
    sorted_mas = quick_sort(mas)
    result = " ".join(map(str, sorted_mas))
    write_f(result, OUTPUT_PATH)

