import unittest
import tracemalloc
import timeit
from Lab_2.Task_3.src.main import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_should_performance_merge_sort_big_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [1, 2, 3, 4, 5]
        temp_array = [0] * len(data)
        expected_data = 4

        # when
        # time test
        start_time = timeit.default_timer()
        result = merge_sort(data, temp_array, 0, len(data) - 1)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = merge_sort(data, temp_array, 0, len(data) - 1)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_merge_sort_small_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [1, 2]
        temp_array = [0] * len(data)
        expected_data = 1

        # when
        # time test
        start_time = timeit.default_timer()
        result = merge_sort(data, temp_array, 0, len(data) - 1)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = merge_sort(data, temp_array, 0, len(data) - 1)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
