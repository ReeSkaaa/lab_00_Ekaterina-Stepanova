from Lab_4.Task_4.src.main import check_brackets
import timeit
import tracemalloc
import unittest


class TestStringMethods(unittest.TestCase):
    def test_should_performance_check_brackets_small_list(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 5
        data = ['[', ']']
        expected_data = 'Success'

        # when
        # time test
        start_time = timeit.default_timer()
        result = check_brackets(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = check_brackets(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_check_brackets_bigger_list(self):
        "Теста затрат времени и памяти"
        # given
        expected_time = 5
        data = ['{', '}', '[', ']']
        expected_data = 'Success'

        # when
        # time test
        start_time = timeit.default_timer()
        result = check_brackets(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = check_brackets(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_check_brackets_hard_list(self):
        "Теста затрат времени и памяти"
        # given
        expected_time = 5
        data = ['[', '(', ')', ']']
        expected_data = 'Success'

        # when
        # time test
        start_time = timeit.default_timer()
        result = check_brackets(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = check_brackets(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_check_brackets_similar_brackets(self):
        "Теста затрат времени и памяти"
        # given
        expected_time = 5
        data = ['(', '(', ')', ')']
        expected_data = 'Success'

        # when
        # time test
        start_time = timeit.default_timer()
        result = check_brackets(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = check_brackets(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_check_brackets_single_bracket(self):
        "Теста затрат времени и памяти"
        # given
        expected_time = 5
        data = ['{']
        expected_data = 1

        # when
        # time test
        start_time = timeit.default_timer()
        result = check_brackets(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = check_brackets(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_check_brackets_single_and_correct_brackets(self):
        "Теста затрат времени и памяти"
        # given
        expected_time = 5
        data = ['{', '[', '}']
        expected_data = 3

        # when
        # time test
        start_time = timeit.default_timer()
        result = check_brackets(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = check_brackets(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_check_brackets_function_brackets(self):
        "Теста затрат времени и памяти"
        # given
        expected_time = 5
        data = ['f', 'o', 'o', '(', 'b', 'a', 'r', ')', ';']
        expected_data = 'Success'

        # when
        # time test
        start_time = timeit.default_timer()
        result = check_brackets(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = check_brackets(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_check_brackets_function_brackets_uncorrect(self):
        "Теста затрат времени и памяти"
        # given
        expected_time = 5
        data = ['f', 'o', 'o', '(', 'b', 'a', 'r', '[', 'i', ')', ';']
        expected_data = 10

        # when
        # time test
        start_time = timeit.default_timer()
        result = check_brackets(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = check_brackets(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
