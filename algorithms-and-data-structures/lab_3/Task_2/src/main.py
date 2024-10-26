from lab_3.Task_2.utils import read_f, write_f


def antiQuickSortPermutation(n):
    perm = [i for i in range(1, n + 1)]

    for i in range(2, n):
        swap(perm, i // 2, i)

    return perm


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


if __name__ == "__main__":
    res_read = read_f("../txtf/input.txt")
    n = int(res_read[0][0])
    result = antiQuickSortPermutation(n)
    write_f("../txtf/output.txt", str(result))
