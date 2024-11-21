import time
import unittest
import tracemalloc
import timeit
from lab_2.Task_3.src.main import merge_sort


class TestInversionsCount(unittest.TestCase):
    def test_should_memory(self):
        "Функция для теста затрат памяти"
        # given

        b = 256
        data = [1, 2, 3, 4, 5]
        temp_array = [0] * len(data)
        # when

        tracemalloc.start()
        result = merge_sort(data, temp_array, 0, len(data) - 1)
        end_time = timeit.default_timer()
        tracemalloc.stop()
        a = tracemalloc.get_traced_memory()[1] / 2 ** 20
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит памяти'
            self.fail(self._formatMessage(standardMsg))
        # given

        b = 256
        data = [10000000000, 2727272772, 2288347, 10102020202]
        temp_array = [0] * len(data)
        # when

        tracemalloc.start()
        result = merge_sort(data, temp_array, 0, len(data) - 1)
        end_time = timeit.default_timer()
        tracemalloc.stop()
        a = tracemalloc.get_traced_memory()[1] / 2 ** 20
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит памяти'
            self.fail(self._formatMessage(standardMsg))
        # given

        b = 256
        data = [10000000000, 2727272772, 2288347, 10102020202, 33487474, 1, 2, 3, 4, 5]
        temp_array = [0] * len(data)
        # when

        tracemalloc.start()
        result = merge_sort(data, temp_array, 0, len(data) - 1)
        end_time = timeit.default_timer()
        tracemalloc.stop()
        a = tracemalloc.get_traced_memory()[1] / 2 ** 20
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит памяти'
            self.fail(self._formatMessage(standardMsg))


def test_should_time(self):
    "Функция для теста затрат времени"
    # given

    b = 2
    data = [1, 2, 3, 4, 5]
    temp_array = [0] * len(data)
    # when

    start_time = timeit.default_timer()
    result = merge_sort(data, temp_array, 0, len(data) - 1)
    end_time = timeit.default_timer()
    a = end_time - start_time
    # then

    if not a <= b:
        standardMsg = 'Превышен лимит времени'
        self.fail(self._formatMessage(standardMsg))
    # given

    b = 2
    data = [2, 7, 9, 2, 1, 100]
    temp_array = [0] * len(data)
    # when

    start_time = timeit.default_timer()
    result = merge_sort(data, temp_array, 0, len(data) - 1)
    end_time = timeit.default_timer()
    a = end_time - start_time
    # then

    if not a <= b:
        standardMsg = 'Превышен лимит времени'
        self.fail(self._formatMessage(standardMsg))

    # given
    b = 2
    data = [1000000, 1939387, 7, 9, 2, 1, 100, 11001010101001]
    temp_array = [0] * len(data)

    # when

    start_time = timeit.default_timer()
    result = merge_sort(data, temp_array, 0, len(data) - 1)
    end_time = timeit.default_timer()
    a = end_time - start_time
    # then

    if not a <= b:
        standardMsg = 'Превышен лимит времени'
        self.fail(self._formatMessage(standardMsg))


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

    result = merge_sort(array, temp_array, 0, len(array) - 1)
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
