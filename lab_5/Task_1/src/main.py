from lab_5.utils import read_f, write_f


def check_heap(n, data):
    flag = 0
    for i in range(1, n // 2 + 1):
        if ((2 * i <= n) and (data[i] > data[2 * i])):
            flag = 1
            break
        if (2 * i + 1 <= n) and (data[i] > data[2 * i + 1]):
            flag = 1
            break

    if flag:
        return 'NO'
    else:
        return 'YES'


if __name__ == "__main__":
    n, data = read_f(1)
    data = list(map(int, data.split()))
    data = [0] + data
    n = int(n)
    result = check_heap(n, data)
    write_f(1, result)
