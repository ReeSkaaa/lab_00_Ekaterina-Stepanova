from Lab_5.Task_5.src.main import do_schedule
import timeit
import tracemalloc
import unittest


class TestShedule(unittest.TestCase):
    def test_should_performance_do_schedule_small_list(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 6
        n = 2
        data = [1, 2, 3, 4, 5]
        expected_data = [(0, 0), (1, 0), (0, 1), (1, 2), (0, 4)]

        # when
        # time test
        start_time = timeit.default_timer()
        result = do_schedule(n, data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = do_schedule(n, data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_do_schedule_bigger_list(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 6
        n = 4
        data = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        expected_data = [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (3, 2),
                         (0, 3), (1, 3), (2, 3), (3, 3), (0, 4), (1, 4), (2, 4), (3, 4)]

        # when
        # time test
        start_time = timeit.default_timer()
        result = do_schedule(n, data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = do_schedule(n, data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
