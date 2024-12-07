from lab_7.utils import read_f, write_f


def lcs(A, B, n, m):
    table = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[n][m]


if __name__ == "__main__":
    data = read_f(4)
    str_1, str_2 = data[1], data[3]
    str_1 = str_1.replace(" ", '')
    str_2 = str_2.replace(" ", '')
    n, m = int(data[0]), int(data[2])
    result = lcs(str_1, str_2, n, m)
    write_f(4, result)
