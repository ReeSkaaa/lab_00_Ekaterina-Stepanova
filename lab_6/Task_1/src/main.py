from lab_6.utils import read_f, write_f

s = set()
answer = []

def add_A(data):
    s.add(data)


def find(data):
    if data in s:
        answer.append('Y')
    else:
        answer.append('N')


def del_D(data):
    s.remove(data)


def do_task(n, a):
    for i in range(n):
        command, data = a[i].split()
        if command == 'A':
            add_A(data)
        elif command == 'D':
            del_D(data)
        elif command == '?':
            find(data)
    return answer


if __name__ == "__main__":
    data = read_f(1)
    n = int(data[0])
    data.pop(0)
    res = do_task(n, data)
    write_f(1, *res)
