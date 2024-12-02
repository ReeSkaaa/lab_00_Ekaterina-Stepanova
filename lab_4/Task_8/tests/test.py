from lab_4.Task_8.src.main import postfix_notation
import timeit
import tracemalloc
import unittest


class TestStringMethods(unittest.TestCase):
    def test_should_performance_postfix_notation(self):
        "Тест затрат времени, памяти и проверка корректного ответа"
        # given
        expected_time = 2
        data = ['8', '9', '+', '1', '7', '-', '*']
        expected_data = -102

        # when
        # time test
        start_time = timeit.default_timer()
        result = postfix_notation(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = postfix_notation(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

if __name__ == '__main__':
    unittest.main()
