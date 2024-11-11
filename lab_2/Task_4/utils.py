def read_f(path):
    with open(path) as f:
        n = int(f.readline())
        second_add = list(map(int, f.readline().split()))
        k = int(f.readline())
        third_add = list(map(int, f.readline().split()))
    return (n, second_add, k,  third_add)


def write_f(path, result):
    with open(path, "w") as f:
        f.write(result)
