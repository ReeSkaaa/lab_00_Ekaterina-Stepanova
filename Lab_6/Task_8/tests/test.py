from Lab_6.Task_8.src.main import main
import timeit
import tracemalloc
import unittest


class TestAlmostHashTable(unittest.TestCase):
    def test_should_performance_almost_hash_table_small_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 5
        data = ['4 0 0 0', '1 1 0 0']
        expected_data = (3, 1, 1)

        # when
        # time test
        start_time = timeit.default_timer()
        result = main(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = main(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_almost_hash_table_similar_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 5
        data = ['1 1 1 1', '1 1 1 1']
        expected_data = (4, 2, 2)

        # when
        # time test
        start_time = timeit.default_timer()
        result = main(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = main(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")

    def test_should_performance_almost_hash_table_similar_big_data(self):
        "Тест затрат времени и памяти, а также проверки корректного ответа"
        # given
        expected_time = 5
        data = ['9 9 9 9', '9 99 9 9']
        expected_data = (139793588186260, 90, 90)

        # when
        # time test
        start_time = timeit.default_timer()
        result = main(data)
        end_time = timeit.default_timer()
        time = end_time - start_time

        # memory test
        tracemalloc.start()
        result = main(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_data)
        self.assertLessEqual(time, expected_time, F"Run time = {time} <= {expected_time}")
        self.assertLessEqual(current, peak, F"Run memory = {current} <= {peak}")


if __name__ == '__main__':
    unittest.main()
