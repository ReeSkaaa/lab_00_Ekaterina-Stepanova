from Lab_3.Task_1.src.main import quick_sort
import timeit
import tracemalloc
import unittest


class TestQuickSort(unittest.TestCase):
    def test_should_performance_quick_sort_big_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12828]
        expected_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12828]

        # when
        # time test
        start_time = timeit.default_timer()
        result = quick_sort(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = quick_sort(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_quick_sort_small_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [8, 9, 1]
        expected_data = [1, 8, 9]

        # when
        # time test
        start_time = timeit.default_timer()
        result = quick_sort(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = quick_sort(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
