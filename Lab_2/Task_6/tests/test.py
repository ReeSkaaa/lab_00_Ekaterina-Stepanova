from Lab_2.Task_6.src.main import find_max_subarray
import timeit
import tracemalloc
import unittest


class TestMaxSubarray(unittest.TestCase):
    def test_should_performance_find_max_subarray_small_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        expected_data = (1, 10, 144)
        data = [0, 121, -2, 1, 4, 2, -1, 0, 0, 9, 10, -5, 2, 3, -2, -2, -4, 1, -1, 1, -1, 0, -1]

        # when
        # time test
        start_time = timeit.default_timer()
        result = find_max_subarray(data, 0, len(data) - 1)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = find_max_subarray(data, 0, len(data) - 1)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
