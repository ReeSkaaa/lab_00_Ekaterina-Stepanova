from lab_3.utils import read_f, write_f


PATH = '../txtf/input.txt'
OUTPUT_PATH = '../txtf/output.txt'


def get_answer(data):
    n, m, k = map(int, data[0].split())
    lines = [''] * n
    for x in range(m):
        s = data[x + 1].strip()
        for y in range(n):
            lines[y] += s[y]

    indexed_lines = [(lines[i], i + 1) for i in range(n)]
    for phase in range(1, k + 1):
        indexed_lines.sort(key=lambda x: x[0][m - phase])

    answer = ' '.join(str(index) for i, index in indexed_lines) + '\n'
    return answer


if __name__ == '__main__':
    data = read_f(7)
    result = get_answer(data)
    write_f(7, result)

