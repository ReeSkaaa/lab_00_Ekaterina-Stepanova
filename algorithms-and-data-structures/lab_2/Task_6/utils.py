def read_f(path):
    with open(path) as f:
        first_add = list(map(int, f.readline().split()))
        second_add = list(map(int, f.readline()))
        third_add = list(f.readline())
    return (first_add, second_add, third_add)


def write_f(path, result):
    with open(path, "w") as f:
        f.write(str("Name: Gazprom" + '\n'))
        f.write(str("Period under review: March 2024" + '\n'))
        f.write('Day start: ' + str(result[0]) + '\n')
        f.write('Day end: ' + str(result[1]) + '\n')
        f.write('Max_sum: ' + str(result[2]))

