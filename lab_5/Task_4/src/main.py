from lab_5.utils import read_f, write_f


class MinHeap:
    def __init__(self, n, data):
        self.heap = data
        self.high = n
        self.swaps = []

    def do_heap_sort(self):
        for i in range(self.high // 2 - 1, -1, -1):
            self.swap(i)
        return len(self.swaps), self.swaps

    def swap(self, ind):
        root = ind
        left_ind = 2 * ind + 1
        right_ind = 2 * ind + 2

        if left_ind < self.high and self.heap[left_ind] < self.heap[root]:
            root = left_ind

        if right_ind < self.high and self.heap[right_ind] < self.heap[root]:
            root = right_ind

        if root != ind:
            self.swaps += [(ind, root)]
            self.heap[ind], self.heap[root] = self.heap[root], self.heap[ind]
            self.swap(root)

if __name__ == "__main__":
    n, data = read_f(4)
    n = int(n)
    data = list(map(int, data.split()))
    heap = MinHeap(n, data).do_heap_sort()
    res = f'{heap[0]}\n'
    res += "\n".join(f'{h[0]} {h[1]}' for h in heap[1])
    write_f(7, res)
