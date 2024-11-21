from lab_3.Task_2.src.main import antiQuickSortPermutation
import timeit
import tracemalloc
import unittest


class TestStringMethods(unittest.TestCase):

    def test_should_time(self):
        "Функция для теста затрат времени"
        # given

        b = 2
        data = 1
        # when

        start_time = timeit.default_timer()
        result = antiQuickSortPermutation(data)
        end_time = timeit.default_timer()
        a = end_time - start_time
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит времени'
            self.fail(self._formatMessage(standardMsg))
        # given

        b = 2
        data = 1500550
        # when

        start_time = timeit.default_timer()
        result = antiQuickSortPermutation(data)
        end_time = timeit.default_timer()
        a = end_time - start_time
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит времени'
            self.fail(self._formatMessage(standardMsg))


def test_should_memory(self):
    "Функция для теста затрат памяти"
    # given

    b = 256
    data = 1
    # when

    tracemalloc.start()
    result = antiQuickSortPermutation(data)
    tracemalloc.stop()
    a = tracemalloc.get_traced_memory()[1] / 2 ** 20
    # then

    if not a <= b:
        standardMsg = 'Превышен лимит памяти'
        self.fail(self._formatMessage(standardMsg))
    # given

    b = 256
    data = 100
    # when

    tracemalloc.start()
    result = antiQuickSortPermutation(data)
    tracemalloc.stop()
    a = tracemalloc.get_traced_memory()[1] / 2 ** 20
    # then

    if not a <= b:
        standardMsg = 'Превышен лимит памяти'
        self.fail(self._formatMessage(standardMsg))
    # given

    b = 256
    data = 130300
    # when

    tracemalloc.start()
    result = antiQuickSortPermutation(data)
    tracemalloc.stop()
    a = tracemalloc.get_traced_memory()[1] / 2 ** 20
    # then

    if not a <= b:
        standardMsg = 'Превышен лимит памяти'
        self.fail(self._formatMessage(standardMsg))


def test_should_single_antiQuick(self):
    # given

    expected_result = [1]
    data = 1
    # when

    result = antiQuickSortPermutation(data)
    # then

    self.assertEqual(result, expected_result)


def test_should_antiQuick(self):
    # given

    expected_result = [1, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50,
                       52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98,
                       100, 25, 51, 13, 53, 27, 55, 7, 57, 29, 59, 15, 61, 31, 63, 2, 65, 33, 67, 17, 69, 35, 71, 9, 73,
                       37, 75, 19, 77, 39, 79, 5, 81, 41, 83, 21, 85, 43, 87, 11, 89, 45, 91, 23, 93, 47, 95, 3, 97, 49,
                       99]
    data = 100
    # when

    result = antiQuickSortPermutation(data)
    # then

    self.assertEqual(result, expected_result)
    # given

    expected_result = [1, 3, 2]
    data = 3
    # when

    start_time = timeit.default_timer()
    result = antiQuickSortPermutation(data)
    end_time = timeit.default_timer()
    print("Время работы программы:", end_time - start_time)
    # then
    self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
