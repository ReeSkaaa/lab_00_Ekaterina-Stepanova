from lab_6.utils import read_f, write_f
class HashSet:
    EMPTY = -1
    DELETED = -2

    def __init__(self, capacity):
        self.capacity = capacity
        self.htable = [self.EMPTY] * capacity
        self.size = 0

    def find_index(self, x):
        def iter(i, h, place_to_insert=-1):
            if i <= self.size + 1:
                if self.htable[h] == self.EMPTY:
                    return (False, place_to_insert if place_to_insert >= 0 else h)
                elif self.htable[h] == self.DELETED:
                    return iter(i + 1, (h + 41) % self.capacity, place_to_insert if place_to_insert >= 0 else h)
                elif self.htable[h] == x:
                    return (True, h)
                else:
                    return iter(i + 1, (h + 41) % self.capacity, place_to_insert)
            else:
                return (False, place_to_insert)

        return iter(0, x % self.capacity)

    def insert(self, x):
        found, h = self.find_index(x)
        if not found:
            self.size += 1
            self.htable[h] = x
            return True
        return False

def main(data):
    al = 1000
    bl = 10**15


    n, x, a, b = map(int, data[0].split())
    ac, bc, ad, bd = map(int, data[1].split())

    set_hash = HashSet(15000017)
    for _ in range(n):
        if not set_hash.insert(x):
            a = (a + ac) % al
            b = (b + bc) % bl
        else:
            a = (a + ad) % al
            b = (b + bd) % bl
        x = (x * a + b) % bl

    return x, a, b

if __name__ == "__main__":
    data = read_f(8)
    res = main(data)
    s = ''
    for i in range(3):
        s+=str(res[i])+' '
    write_f(8, s)

