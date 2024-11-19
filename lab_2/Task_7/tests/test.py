import random
from lab_2.Task_7.src.main import find_max_subarray
import time
import unittest
from lab_2.utils import read_f
import tracemalloc

def test_time():
    "Функция для проверки затрат памяти и времени при данных, взятых пользователем из файла"
    # given
    read = read_f(7)
    n = int(read[0])
    # when
    t_start = time.perf_counter()
    tracemalloc.start()
    a = [random.randint(-10 ** 3, 10 ** 3) for i in range(n)]
    res = find_max_subarray(a, n)
    t_start = time.perf_counter()
    # then
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
    tracemalloc.stop()


class TestStringMethods(unittest.TestCase):
    def test_should__max_subarray(self):
        # given
        data = [-1, 2, 3, -9]
        expected_result = 5
        # when
        t_start = time.perf_counter()
        res = find_max_subarray(data, len(data) - 1)
        result = res[0]
        t_start = time.perf_counter()
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        # then
        self.assertEqual(result, expected_result)

        # given
        data = [2, -1, 2, 3, -9]
        expected_result = 6
        # when
        t_start = time.perf_counter()
        res = find_max_subarray(data, len(data) - 1)
        result = res[0]
        t_start = time.perf_counter()
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        # then
        self.assertEqual(result, expected_result)


    def test_should_no_max_subarray(self):
        # given
        data = [-1, -2, -3]
        expected_result = 0
        # when
        t_start = time.perf_counter()
        res = find_max_subarray(data, len(data) - 1)
        result = res[0]
        t_start = time.perf_counter()
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        # then
        self.assertEqual(result, expected_result)

