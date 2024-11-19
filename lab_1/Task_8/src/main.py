from lab_1.utils import read_f, write_f
PATH = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'
answer = []


def mister_swap(a, n):
    for i in range(n - 1):
        min_id = i
        min = a[i]
        for j in range(i + 1, n):
            if a[j] < min:
                min = a[j]
                min_id = j
        if min_id != i:
            a[i], a[min_id] = a[min_id], a[i]
            answer.append(f'Swap elements at indices {i + 1} and {min_id + 1}.\n')
    return answer

if __name__ == '__main__':
    n, read_res = read_f(8)
    data = list(map(int, read_res.split()))
    n = int(n)
    if (3 <= n <= 5 * 10 ** 3):
        mister_swap(data, n)
        answer.append('No more swaps needed.')
        write_f(8, *answer)
        answer.clear()
    else:
        print('Error.Try again')
