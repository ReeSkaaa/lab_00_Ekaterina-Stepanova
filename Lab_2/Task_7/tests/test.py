from Lab_2.Task_7.src.main import find_max_subarray
import timeit
import unittest
import tracemalloc


class TestFindMaxSubarray(unittest.TestCase):
    def test_should_performance_find_max_subarray_small_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [-1, -2, -3]
        expected_data = (0, 1, 0)

        # when
        # time test
        start_time = timeit.default_timer()
        result = find_max_subarray(data, len(data) - 1)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = find_max_subarray(data, len(data) - 1)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


    def test_should_performance_find_max_subarray_big_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [-1, -2, -3, 10, 6, 8, 9, -120]
        expected_data = (33, 3, 6)

        # when
        # time test
        start_time = timeit.default_timer()
        result = find_max_subarray(data, len(data) - 1)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = find_max_subarray(data, len(data) - 1)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
