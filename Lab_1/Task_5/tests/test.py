from Lab_1.Task_5.src.main import selection_sort
import timeit
import unittest
import tracemalloc


class TestSelectionSort(unittest.TestCase):
    def test_should_performance_selection_sort_single_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 2
        data = [[1], 1]
        expected_data = [1]

        # when
        # time test
        start_time = timeit.default_timer()
        result = selection_sort(data[0], data[1])
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = selection_sort(data[0], data[1])
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_selection_sort_small_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 2
        data = [[2, 3, 1], 3]
        expected_data = [1, 2, 3]

        # when
        # time test
        start_time = timeit.default_timer()
        result = selection_sort(data[0], data[1])
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = selection_sort(data[0], data[1])
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_selection_sort_big_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 2
        data = [[2, 3, 1, 6, 5, 4, 8, 7, 9, 10], 10]
        expected_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # when
        # time test
        start_time = timeit.default_timer()
        result = selection_sort(data[0], data[1])
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = selection_sort(data[0], data[1])
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
