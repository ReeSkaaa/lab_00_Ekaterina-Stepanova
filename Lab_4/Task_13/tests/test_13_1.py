from Lab_4.Task_13.src.main_13_1 import Stack
import timeit
import tracemalloc
import unittest


class TestStack(unittest.TestCase):
    "Тест затрат времени, памяти и проверка корректного ответа"

    def test_should_performance_empty_stack(self):
        # given
        expected_time = 2
        self.stack = Stack()
        expected_data = True

        # when
        # time test
        start_time = timeit.default_timer()
        result = self.stack.isEmpty()
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = self.stack.isEmpty()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_push(self):
        "Тест затрат времени, памяти и проверка корректного ответа"
        # given
        expected_time = 1
        self.stack = Stack()
        char = 'a'
        expected_data = None

        # when
        # time test
        start_time = timeit.default_timer()
        self.stack.push(char)
        result = self.assertFalse(self.stack.isEmpty())
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        self.stack.push(char)
        result = self.assertFalse(self.stack.isEmpty())
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
