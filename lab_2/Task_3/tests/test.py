import time
import unittest
import tracemalloc
import timeit
from lab_2.Task_3.src.main import merge_sort
from lab_2.utils import read_f


def test_time_memory():
    "Функция для проверки затрат памяти и времени при данных, взятых пользователем из файла"
    # given

    _, read = read_f(3)
    data = list(map(int, read.split()))
    a = data.copy()
    # when

    start_time = timeit.default_timer()
    tracemalloc.start()
    result = merge_sort(data, a, 0, len(data) - 1)
    end_time = timeit.default_timer()
    # then

    print("Время работы программы:", end_time - start_time)
    print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
    tracemalloc.stop()


class TestInversionsCount(unittest.TestCase):
    def test_should_no_inversions(self):
        # given
        array = [1, 2, 3, 4, 5]
        temp_array = [0] * len(array)
        # when
        start_time = time.perf_counter()
        result = merge_sort(array, temp_array, 0, len(array) - 1)
        end_time = time.perf_counter()
        print(f"Время работы: {end_time - start_time:.4f} секунд")
        # then
        self.assertEqual(result, 0)

    def test_should_reverse_sorted(self):
        # given
        array = [5, 4, 3, 2, 1]
        temp_array = [0] * len(array)
        # when
        start_time = time.perf_counter()
        result = merge_sort(array, temp_array, 0, len(array) - 1)
        end_time = time.perf_counter()
        print(f"Время работы: {end_time - start_time:.4f} секунд")
        # then
        self.assertEqual(result, 10)

    def test_should_empty_array(self):
        # given
        array = []
        temp_array = []
        # when
        start_time = time.perf_counter()
        result = merge_sort(array, temp_array, 0, len(array) - 1)
        end_time = time.perf_counter()
        print(f"Время работы: {end_time - start_time:.4f} секунд")
        # then
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
