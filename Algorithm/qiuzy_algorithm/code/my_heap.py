def heapify(tree, n, i):
    """
    递归的方式实现。
    :param tree: 完全二叉树/列表
    :param n: 完全二叉树的结点数
    :param i: 当前结点，
    :return: None
    """
    # 设一个最大值
    largest = i
    left = 2 * i + 1  # 左子结点：left = 2*i + 1
    right = 2 * i + 2  # 右子结点：right = 2*i + 2

    # 如果左子结点存在且比父结点大，修改最大值
    if left < n and tree[largest] < tree[left]:
        largest = left

    # 如果右结点存在且比父结点大，修改最大值
    if right < n and tree[largest] < tree[right]:
        largest = right

    # 如果最大值不是当前结点，则进行交换
    if largest != i:
        tree[i], tree[largest] = tree[largest], tree[i]
        # Heapify the root.
        heapify(tree, n, largest)

def heap_sort(tree):
    n = len(tree)

    # 构建一个小 (n-2) //2 可以写成n // 2 - 1，从最右的分支结点开始
    for i in range(n // 2 - 1, -1, -1):
        heapify(tree, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        tree[i], tree[0] = tree[0], tree[i]
        heapify(tree, i, 0)


if __name__ == '__main__':
    example_tree = [12, 11, 13, 5, 6, 7]
    heap_sort(example_tree)
    print(example_tree)
