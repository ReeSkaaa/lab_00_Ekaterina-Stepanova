import tracemalloc
import time

def read_fp(path):
    """Функция чтения данных файла и возвращение строк в виде списка."""
    with open(path, 'r', encoding='utf-8') as f:
        return f.readlines()

def write_f(path, result):
    """Запись данных в файл."""
    with open(path, 'w', encoding='utf-8') as file:
        file.write(result)

def measure_time_and_memory(func):
    """Декоратор для измерения времени выполнения и памяти."""
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"Время работы: {end_time - start_time:.4f} секунд")
        print(f"Максимальная память: {peak / 1024:.2f} KB")

        return result
    return wrapper
