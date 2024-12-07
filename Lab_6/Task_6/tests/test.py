from Lab_6.Task_6.src.main import iterativeFib, fib_come_back
import timeit
import tracemalloc
import unittest


class TestFibComeBack(unittest.TestCase):
    def test_should_performance_fib_comeback_large_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 2
        n = 8
        data = [1, 2, 3, 4, 5, 6, 7, 8]
        expected_data = ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes']

        # when
        # time test
        start_time = timeit.default_timer()
        all_fib_num = iterativeFib(set(), 5000)
        result = fib_come_back(all_fib_num, n, data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        all_fib_num = iterativeFib(set(), 5000)
        result = fib_come_back(all_fib_num, n, data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_fib_comeback_single_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 2
        n = 1
        data = [1]
        expected_data = ['Yes']

        # when
        # time test
        start_time = timeit.default_timer()
        all_fib_num = iterativeFib(set(), 5000)
        result = fib_come_back(all_fib_num, n, data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        all_fib_num = iterativeFib(set(), 5000)
        result = fib_come_back(all_fib_num, n, data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_fib_comeback_small_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 2
        n = 3
        data = [1, 2, 3]
        expected_data = ['Yes', 'Yes', 'Yes']

        # when
        # time test
        start_time = timeit.default_timer()
        all_fib_num = iterativeFib(set(), 5000)
        result = fib_come_back(all_fib_num, n, data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        all_fib_num = iterativeFib(set(), 5000)
        result = fib_come_back(all_fib_num, n, data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_fib_comeback_similar_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 2
        n = 5
        data = [-1, -1, -1, -1, -1]
        expected_data = ['No', 'No', 'No', 'No', 'No']

        # when
        # time test
        start_time = timeit.default_timer()
        all_fib_num = iterativeFib(set(), 5000)
        result = fib_come_back(all_fib_num, n, data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        all_fib_num = iterativeFib(set(), 5000)
        result = fib_come_back(all_fib_num, n, data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
