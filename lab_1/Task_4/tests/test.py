from lab_1.Task_4.src.main import lin_searh
import timeit
import tracemalloc
import unittest


class TestStringMethods(unittest.TestCase):
    def test_should_memory(self):
        "Функция для теста затрат памяти"
        # given

        b = 256
        data = [[1, 2, 3], 3, 1]
        # when

        tracemalloc.start()
        result = lin_searh(data[0], data[1], data[2])
        tracemalloc.stop()
        a = tracemalloc.get_traced_memory()[1] / 2 ** 20
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит памяти'
            self.fail(self._formatMessage(standardMsg))
    def test_should_time(self):
        "Функция для теста затрат времени"
        # given

        b = 2
        data = [[1, 2, 3], 3, 1]
        # when

        start_time = timeit.default_timer()
        result = lin_searh(data[0], data[1], data[2])
        end_time = timeit.default_timer()
        a = end_time - start_time
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит времени'
            self.fail(self._formatMessage(standardMsg))

    def test_should_insertion_sort(self):
        # given

        expected_result = (1, [0])
        data = [[1, 2, 3], 3, 1]
        # when

        result = lin_searh(data[0], data[1], data[2])
        # then

        self.assertEqual(result, expected_result)
        # given

        expected_result = (2, [3, 4])
        data = [[1, 2, 3, 7, 7, 5], 6, 7]

        # when
        start_time = timeit.default_timer()
        result = lin_searh(data[0], data[1], data[2])
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
