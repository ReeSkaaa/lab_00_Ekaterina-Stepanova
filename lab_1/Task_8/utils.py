def read_f(path):
    with open(path) as f:
        first_add = int(f.readline())
        second_add = list(map(int, f.readline().split()))
        third_add = list(f.readline())
    return (first_add, second_add, third_add)


def write_f(path, result_1, result_2):
    with open(path, "w") as f:
        f.write(result_1)
        f.write(result_2)
