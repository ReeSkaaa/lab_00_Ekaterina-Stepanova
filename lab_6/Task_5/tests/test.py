from lab_6.Task_5.src.main import do_task
import timeit
import tracemalloc
import unittest


class TestPresidentialElections(unittest.TestCase):
    def test_should_performance_presidential_elections_single_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 2
        n = 1
        data = ['bur 1']
        expected_data = [('bur', 1)]

        # when
        # time test
        start_time = timeit.default_timer()
        result = do_task(n, data, s ={})
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = do_task(n, data, s={})
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_presidential_elections_big_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 2
        n = 6
        data = ['ivanov 100', 'ivanov 500', 'ivanov 300', 'petr 70', 'tourist 1', 'tourist 2']
        expected_data = [('ivanov', 900), ('petr', 70), ('tourist', 3)]

        # when
        # time test
        start_time = timeit.default_timer()
        result = do_task(n, data, s={})
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = do_task(n, data, s={})
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_presidential_elections_small_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 2
        n = 5
        data = ['McCain 10', 'McCain 5', 'Obama 9', 'Obama 8', 'McCain 1']
        expected_data = [('McCain', 16), ('Obama', 17)]

        # when
        # time test
        start_time = timeit.default_timer()
        result = do_task(n, data, s={})
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = do_task(n, data, s={})
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
