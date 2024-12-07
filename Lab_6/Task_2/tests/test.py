from Lab_6.Task_2.src.main import do_task
import timeit
import tracemalloc
import unittest


class TestPhoneBook(unittest.TestCase):
    def test_should_performance_check_do_task_phone_book_large_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 6
        n = 12
        data = ['add 911 police', 'add 76213 Mom', 'add 17239 Bob', 'find 76213', 'find 910', 'find 911', 'del 910',
                'del 911', 'find 911', 'find 76213', 'add 76213 daddy', 'find 76213']
        expected_data = ['Mom', 'not found', 'police', 'not found', 'Mom', 'daddy']

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

    def test_should_performance_check_do_task_phone_book_smaller_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 6
        n = 8
        data = ['find 3839442', 'add 123456 me', 'add 0 granny', 'find 0', 'find 123456', 'del 0', 'del 0', 'find 0']
        expected_data = ['not found', 'granny', 'me', 'not found']

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
