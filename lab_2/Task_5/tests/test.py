from lab_2.Task_5.src.main import majority_element
import time
import tracemalloc
import timeit
import unittest
from lab_2.utils import read_f


def test_time_memory():
    "Функция для проверки затрат памяти и времени при данных, взятых пользователем из файла"
    # given
    n, read = read_f(5)
    # when
    start_time = timeit.default_timer()
    tracemalloc.start()
    data = list(map(int, read.split()))
    result = majority_element(data, int(n))
    end_time = timeit.default_timer()
    # then
    print("Время работы программы:", end_time - start_time)
    print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
    tracemalloc.stop()

class TestStringMethods(unittest.TestCase):
    def test_should_majority_element(self):
        # given
        expected_result = 0
        data = [[1, 2, 3, 4], 4]

        # when
        start_time = time.perf_counter()
        result = majority_element(data[0], data[1])
        end_time = time.perf_counter()
        print(f"Время работы: {end_time - start_time:.4f} секунд")

        # then
        self.assertEqual(result, expected_result)

        # given
        expected_result = 1
        data = [[7, 1, 1], 3]

        # when
        start_time = time.perf_counter()
        result = majority_element(data[0], data[1])
        end_time = time.perf_counter()
        print(f"Время работы: {end_time - start_time:.4f} секунд")

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
