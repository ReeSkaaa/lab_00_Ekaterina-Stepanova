from Lab_7.utils import read_f, write_f


def change_coins(money, coins):
    table = [float('inf') for _ in range(money + 1)]
    table[0] = 0
    for m in range(1, money + 1):
        for c in coins:
            if c <= m:
                table[m] = min(table[m], 1 + table[m - c])
    return table[money]


if __name__ == "__main__":
    data, vector = read_f(1)
    data = list(map(int, data.split()))
    money, n = data[0], data[1]
    coins = list(map(int, vector.split()))
    result = change_coins(money, coins)
    print(result)
    write_f(1, result)
