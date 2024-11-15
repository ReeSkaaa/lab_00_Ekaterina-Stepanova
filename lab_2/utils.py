def read_f(path):
    """Читает данные из файла и возвращает их в виде списка целых чисел."""
    with open(path, "r") as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))
    return n, arr

def write_f(path, result):
    """Записывает результат в файл."""
    with open(path, "w") as file:
        if isinstance(result, list):
            file.write(" ".join(map(str, result)) + "\n")
        else:
            file.write(str(result) + "\n")