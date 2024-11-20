from lab_3.Task_1.src.main import quick_sort
import timeit
import time
import tracemalloc
from lab_2.utils import read_f
import unittest


def test_time():
    "Функция для проверки времени при данных, взятых пользователем из файла"
    # given

    _, read = read_f(1)
    data = list(map(int, read.split()))
    # when

    start_time = timeit.default_timer()

    result = quick_sort(data)
    end_time = timeit.default_timer()
    # then

    print("Время работы программы:", end_time - start_time)

def test_memory():
    "Функция для проверки затрат памяти при данных, взятых пользователем из файла"
    # given

    _, read = read_f(1)
    data = list(map(int, read.split()))
    # when
    tracemalloc.start()
    result = quick_sort(data)
    # then
    print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
    tracemalloc.stop()
class TestStringMethods(unittest.TestCase):
    def test_should_no_elem_binary_search(self):
        # given
        expected_result = []
        data = []

        # when
        start_time = timeit.default_timer()
        result = quick_sort(data)
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)
        # then
        self.assertEqual(result, expected_result)

    def test_should_single_binary_search(self):
        # given
        expected_result = [1]
        data = [1]

        # when
        start_time = timeit.default_timer()
        result = quick_sort(data)
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)
        # then
        self.assertEqual(result, expected_result)

    def test_should_binary_search(self):
        # given
        expected_result = [1, 2, 9]
        data = [1, 9, 2]

        # when
        start_time = timeit.default_timer()
        result = quick_sort(data)
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)
        # then
        self.assertEqual(result, expected_result)

        # given
        expected_result = [1, 2, 3, 4, 5]
        data = [1, 3, 2, 5, 4]

        # when
        start_time = timeit.default_timer()
        result = quick_sort(data)
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)
        # then
        self.assertEqual(result, expected_result)

    def test_should_long_binary_search(self):
        # given
        expected_result = [100, 200, 700, 8000, 9999999, 100000000000000000]
        data = [200, 100, 100000000000000000, 700, 8000, 9999999]

        # when
        start_time = timeit.default_timer()
        result = quick_sort(data)
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)
        # then
        self.assertEqual(result, expected_result)

    def test_should_sorted_binary_search(self):
        # given
        expected_result = [1, 2, 3]
        data = [1, 2, 3]

        # when
        start_time = timeit.default_timer()
        result = quick_sort(data)
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)
        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
