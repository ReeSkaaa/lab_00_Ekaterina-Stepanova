from lab_2.Task_1.src.main import merge_sort
from lab_2.utils import read_f, write_f
import timeit
import tracemalloc
import unittest

def test_time_memory():
    "Функция для проверки затрат памяти и времени при данных, взятых пользователем из файла"
    # given

    _, read = read_f(task=1)
    array = list(map(int, read.split()))
    # when

    start_time = timeit.default_timer()
    tracemalloc.start()
    merge_sort(array, 0, len(array) - 1)
    end_time = timeit.default_timer()
    # then

    print("Время работы программы:", end_time - start_time)
    print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
    tracemalloc.stop()



class TestStringMethods(unittest.TestCase):

    def test_should_empty_massive(self):
        # given
        data = []
        expected_result = None
        # when
        result = merge_sort(data, 0, len(data) - 1)
        # then
        self.assertEqual(None, result)

    def test_should_already_sorted(self):
        # given
        data = [1, 2, 3, 4]
        expected_result = [1, 2, 3, 4]

        # when
        result = merge_sort(data, 0, len(data) - 1)
        # then
        self.assertEqual(result, expected_result)

    def test_should_merge_sort(self):
        # given
        data = [12, 11, 13, 5, 6, 7]
        expected_result = [5, 6, 7, 11, 12, 13]
        # when
        result = merge_sort(data, 0, len(data) - 1)
        # then
        self.assertEqual(result, expected_result)

    def test_should_reverse_sorted(self):
        # given
        data = [4, 3, 2, 1]
        expected_result = [1, 2, 3, 4]
        # when

        result = merge_sort(data, 0, len(data) - 1)
        # then
        self.assertEqual(result, expected_result)
    def test_should_large_numbers(self):
        # given
        data = [1000000000, 9999998, 1000000000]
        expected_result = [9999998, 1000000000, 1000000000]
        # when
        result = merge_sort(data, 0, len(data) - 1)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
