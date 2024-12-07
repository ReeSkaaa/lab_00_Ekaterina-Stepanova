from Lab_1.Task_6.src.main import bubble_sort
import timeit
import unittest
import tracemalloc


class TestBubbleSort(unittest.TestCase):
    def test_should_performance_insertion_sort_similar_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [1, 1, 1, 1]
        expected_data = [1, 1, 1, 1]

        # when
        # time test
        start_time = timeit.default_timer()
        result = bubble_sort(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = bubble_sort(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_insertion_sort_empty_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = []
        expected_data = []

        # when
        # time test
        start_time = timeit.default_timer()
        result = bubble_sort(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = bubble_sort(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_insertion_sort_small_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [2, 1, 3]
        expected_data = [1, 2, 3]

        # when
        # time test
        start_time = timeit.default_timer()
        result = bubble_sort(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = bubble_sort(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
