from Lab_1.Task_9.src.main import binary_addition
import timeit
import unittest
import tracemalloc


class TestBinaryAddition(unittest.TestCase):
    def test_should_performance_binary_addition_small_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [[1, 0], [0, 1]]
        expected_data = '11'

        # when
        # time test
        start_time = timeit.default_timer()
        result = binary_addition(data[0], data[1])
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = binary_addition(data[0], data[1])
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_binary_addition_single_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [[1], [0]]
        expected_data = '1'

        # when
        # time test
        start_time = timeit.default_timer()
        result = binary_addition(data[0], data[1])
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = binary_addition(data[0], data[1])
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_binary_addition_big_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = [[1, 0, 0, 0], [1]]
        expected_data = '1001'

        # when
        # time test
        start_time = timeit.default_timer()
        result = binary_addition(data[0], data[1])
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = binary_addition(data[0], data[1])
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
