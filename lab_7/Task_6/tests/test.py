from lab_7.Task_6.src.main import get_lis
import timeit
import tracemalloc
import unittest


class TestChangeCoins(unittest.TestCase):
    def test_should_performance_get_lis_big_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 2
        data = [3, 29, 5, 5, 28, 6]
        expected_data = [3, 5, 28]

        # when
        # time test
        start_time = timeit.default_timer()
        result = get_lis(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = get_lis(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_get_lis_small_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 2
        data = [1, 0, 3, 0]
        expected_data = [1, 3]

        # when
        # time test
        start_time = timeit.default_timer()
        result = get_lis(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = get_lis(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
