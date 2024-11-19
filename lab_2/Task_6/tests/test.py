from lab_2.Task_6.src.main import find_max_subarray
import timeit
from lab_2.utils import read_f
import tracemalloc
import unittest
def test_time_memory():
    "Функция для проверки затрат памяти и времени при данных, взятых пользователем из файла"
    # given
    read_ = read_f(6)
    data = list(map(int, read_[0].split()))
    # when
    start_time = timeit.default_timer()
    tracemalloc.start()
    s = find_max_subarray(data, 0, len(data) - 1)
    end_time = timeit.default_timer()
    # then
    print("Время работы программы:", end_time - start_time)
    print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
    tracemalloc.stop()