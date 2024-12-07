from Lab_3.Task_7.src.main import get_answer
import timeit
import tracemalloc
import unittest


class TestStringMethods(unittest.TestCase):
    def test_should_performance_get_answer_data(self):
        "Функция для теста затрат памяти"
        # given
        expected_time = 2
        data = ['3 3 1', 'bab', 'bba', 'baa']
        expected_data = '2 3 1\n'

        # when
        # time test
        start_time = timeit.default_timer()
        result = get_answer(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = get_answer(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
