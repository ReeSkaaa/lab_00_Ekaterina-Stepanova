from Lab_6.Task_1.src.main import do_task, answer
import timeit
import tracemalloc
import unittest


class TestSetCommands(unittest.TestCase):
    def test_should_performance_set(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 2
        n = 8
        data = ['A 2', 'A 5', 'A 3', '? 2', '? 4', 'A 2', 'D 2', '? 2']
        expected_data = ['Y', 'N', 'N', 'Y', 'N', 'N']

        # when
        # time test
        start_time = timeit.default_timer()
        result = do_task(n, data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = do_task(n, data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
