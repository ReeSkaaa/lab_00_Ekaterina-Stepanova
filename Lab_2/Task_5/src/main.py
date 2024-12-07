from Lab_2.utils import read_f, write_f


def majority_element(a, n):
    count_map = {}
    for num in a:
        if num in count_map:
            count_map[num] += 1
            if count_map[num] > n // 2:
                return 1
        else:
            count_map[num] = 1
    return 0


if __name__ == "__main__":
    n, read = read_f(5)
    data = list(map(int, read.split()))
    result = majority_element(data, int(n))
    write_f(5, str(result))
