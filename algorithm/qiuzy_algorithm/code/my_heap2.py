def heap_sort(lst):
    def sift_down(start, end):
        """最大堆调整"""
        # 把每一个分支结点当做一个“小堆”的根结点
        root = start
        while True:
            # 左子结点
            child = 2 * root + 1
            if child > end:
                break
            # 如果右子节点存在且左子节点比右子节点小，那么调整child的值
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            # 如果当前节点不是最大值，那么进行交换
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

    # 创建最大堆
    for start in range((len(lst) - 2) // 2, -1, -1):
        sift_down(start, len(lst) - 1)
    print(lst)
    # 堆排序
    for end in range(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(0, end - 1)
    return lst


if __name__ == "__main__":
    example = [9, 2, 1, 7, 6, 8, 5, 3, 4]
    res = heap_sort(example)
    print(res)
