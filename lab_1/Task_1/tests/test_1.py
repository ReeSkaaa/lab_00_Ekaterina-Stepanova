from task_1 import insertion_sort, main
import timeit
def test_time():
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Время работы программы:", end_time - start_time)

def test_insertion_sort():
    assert insertion_sort([2, 3, 1], 3) == [1, 2, 3]
    assert insertion_sort([31, 41, 59, 26, 41, 58], 6) == [26, 31, 41, 41, 58, 59]
    assert insertion_sort([1, 2], 2) == [1, 2]
