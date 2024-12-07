from Lab_7.Task_1.src.main import change_coins
import timeit
import tracemalloc
import unittest


class TestChangeCoins(unittest.TestCase):
    def test_should_performance_change_coins_small_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 1
        data = [2, [1, 3, 4]]
        expected_data = 2

        # when
        # time test
        start_time = timeit.default_timer()
        result = change_coins(data[0], data[1])
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = change_coins(data[0], data[1])
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_change_coins_big_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 1
        data = [34, [1, 3, 4]]
        expected_data = 9

        # when
        # time test
        start_time = timeit.default_timer()
        result = change_coins(data[0], data[1])
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = change_coins(data[0], data[1])
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
