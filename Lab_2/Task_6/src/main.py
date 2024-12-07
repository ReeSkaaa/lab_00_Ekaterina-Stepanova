from Lab_2.utils import read_f, write_f


def find_max_subarray(a, low, high):
    if high == low:
        return (low, high, a[low])
    else:
        mid = (low + high) // 2
        (leftlow, lefthigh, leftsum) = find_max_subarray(a, low, mid)
        (rightlow, righthigh, rightsum) = find_max_subarray(a, mid + 1, high)
        (crosslow, crosshigh, crosssum) = find_max_crossing_subarray(a, low, mid, high)
        if leftsum >= rightsum and leftsum >= crosssum:
            return (leftlow, lefthigh, leftsum)
        elif rightsum >= leftsum and rightsum >= crosssum:
            return (rightlow, righthigh, rightsum)
        else:
            return (crosslow, crosshigh, crosssum)


def find_max_crossing_subarray(a, low, mid, high):
    leftsum = -10 ** 10
    maxleft, maxright = 0, 0
    sum = 0
    for i in range(mid, low, -1):
        sum += a[i]
        if sum > leftsum:
            leftsum = sum
            maxleft = i
    rightsum = -10 ** 10
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += a[j]
        if sum > rightsum:
            rightsum = sum
            maxright = j
    return (maxleft, maxright, leftsum + rightsum)


if __name__ == "__main__":
    read_ = read_f(6)
    data = list(map(int, read_[0].split()))
    s = find_max_subarray(data, 0, len(data) - 1)
    answer = ["Name: Gazprom",
              "Period under review: March 2024",
              "Day start: " + str(s[0]), "Day end: " + str(s[1]), "Max_sum: " + str(s[2])]
    write_f(6, *answer)
