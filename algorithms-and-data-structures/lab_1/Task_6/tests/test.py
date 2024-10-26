from lab_1.Task_6.src.task_6 import bubble_sort, main
import timeit


def test_time():
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Время работы программы:", end_time - start_time)


def test_bubble():
    assert bubble_sort([1]) == [1]
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble_sort([7, 8, 1, 2, 3, 1]) == [1, 1, 2, 3, 7, 8]
