from Lab_7.utils import read_f, write_f


def edit_dist(s1, s2):
    m, n = len(s1), len(s2)
    prev = list(range(n + 1))

    # Rest of the rows
    for i in range(1, m + 1):
        curr = [i]  # j = 0
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                curr.append(prev[j - 1])
            else:
                curr.append(1 + min(curr[-1], prev[j], prev[j - 1]))
        prev = curr
    return prev[n]


if __name__ == "__main__":
    str_1, str_2 = read_f(3)
    result = edit_dist(str_1, str_2)
    write_f(3, result)
