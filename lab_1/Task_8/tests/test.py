from lab_1.Task_8.src.task_8 import main
import timeit


def test_time():
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Время работы программы:", end_time - start_time)


