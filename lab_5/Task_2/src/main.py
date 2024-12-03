from lab_5.utils import read_f, write_f


def find_tree_height(n, tree):
    node_heights = dict() # высоты всех вершин в дереве
    max_height = 0 # текущая максимальна высота дерева
    for node in tree: # перебираем все вершины в дереве
        curr_node = node
        curr_height = 1
        while True: # для каждой вершины находим высоту
            if curr_node == -1:
                break
            curr_node = tree[curr_node]
            cached_node_height = node_heights.get(curr_node, None)
            if cached_node_height is not None:
                curr_height += cached_node_height
                break
            curr_height += 1
        if node_heights.get(node, None) is None:
            node_heights[node] = curr_height
        if curr_height > max_height:
            max_height = curr_height
    return max_height


if __name__ == "__main__":
    n, data = read_f(2)
    a = find_tree_height(1, [-1])
    tree = list(map(int, data.split()))
    result = find_tree_height(int(n), tree)
    write_f(2, result)