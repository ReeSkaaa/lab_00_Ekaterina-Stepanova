from Lab_1.utils import read_f, write_f



def lin_searh(a, n, v):
    res = []
    k = 0
    for i in range(0, n):
        if a[i] == v:
            k += 1
            res.append(i)
    return k, res

if __name__ == '__main__':
    n, read, elem = read_f(4)
    data = list(map(int, read.split()))
    result = lin_searh(data, int(n), int(elem))
    result = list(result)
    write_f(4, *result)