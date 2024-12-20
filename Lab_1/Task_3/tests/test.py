from Lab_1.Task_3.src.main import insertion_sort
import timeit
import unittest
import tracemalloc


class TestInsertionSort(unittest.TestCase):
    def test_should_performance_insertion_sort_similar_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [[1, 1, 1], 3]
        expected_data = [1, 1, 1]

        # when
        # time test
        start_time = timeit.default_timer()
        result = insertion_sort(data[0], int(data[1]))
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = insertion_sort(data[0], int(data[1]))
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
        data = [[1, 2, 3], 3]
        expected_data = [3, 2, 1]

        # when
        # time test
        start_time = timeit.default_timer()
        result = insertion_sort(data[0], int(data[1]))
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = insertion_sort(data[0], int(data[1]))
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_insertion_sort_big_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 12828], 10]
        expected_data = [12828, 9, 8, 7, 6, 5, 4, 3, 2, 1]

        # when
        # time test
        start_time = timeit.default_timer()
        result = insertion_sort(data[0], int(data[1]))
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = insertion_sort(data[0], int(data[1]))
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
