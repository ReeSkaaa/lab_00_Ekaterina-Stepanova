from lab_1.Task_8.src.main import mister_swap
from lab_1.utils import read_f
import tracemalloc
import unittest
import timeit

def test_time_memory():
    "Функция для проверки затрат памяти и времени при данных, взятых пользователем из файла"

    # given
    n, read_res = read_f(8)
    data = list(map(int, read_res.split()))
    # when
    start_time = timeit.default_timer()
    tracemalloc.start()
    mister_swap(data, int(n))
    end_time = timeit.default_timer()
    # then
    print("Время работы программы:", end_time - start_time)
    print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
    tracemalloc.stop()

