from lab_6.utils import read_f, write_f

phone_book = {}

def add_(entry):
    phone_number, name = entry.split()
    phone_book[phone_number] = name


def del_(phone_num):
    phone_book.pop(phone_num, '')

def do_task(n, a):
    answer = []
    for i in range(n):
        command, data = a[i].split(maxsplit=1)
        if command == 'add':
            add_(data)
        elif command == 'del':
            del_(data)
        elif command == 'find':
            answer.append(phone_book.get(data, 'not found'))
    return answer


if __name__ == "__main__":
    data = read_f(2)
    n = int(data[0])
    data.pop(0)
    res = do_task(n, data)
    write_f(2, *res)
