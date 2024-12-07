from Lab_3.Task_2.src.main import antiQuickSortPermutation
import timeit
import tracemalloc
import unittest


class TestAntiQuickSortPermutation(unittest.TestCase):
    def test_should_performance_antiQuickSortPermutation_small_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = 3
        expected_data = [1, 3, 2]

        # when
        # time test
        start_time = timeit.default_timer()
        result = antiQuickSortPermutation(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = antiQuickSortPermutation(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_antiQuickSortPermutation_small_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = 10
        expected_data = [1, 4, 6, 8, 10, 5, 3, 7, 2, 9]

        # when
        # time test
        start_time = timeit.default_timer()
        result = antiQuickSortPermutation(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = antiQuickSortPermutation(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_antiQuickSortPermutation_empty_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = 0
        expected_data = []

        # when
        # time test
        start_time = timeit.default_timer()
        result = antiQuickSortPermutation(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = antiQuickSortPermutation(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
