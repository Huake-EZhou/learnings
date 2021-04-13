class Solution:
    """
    left:小于基准值的元素索引
    right: 大于基准值的元素索引
    """

    def quick_sort(self, lst):
        # 序列最后一个元素的索引=序列长度-1
        return self.qsort_rec(lst, 0, len(lst) - 1)

    def qsort_rec(self, lst, left, right):
        # 特殊情况：序列只有一个元素或者没有为空
        if left >= right:
            return lst

        # 以最左边的元素为标准值
        i = left
        j = right
        # 用一个变量存储，从而留出一个空位
        pivot = lst[i]
        while i < j:
            # 从右边找出一个比pivot小的数
            while i < j and lst[j] >= pivot:
                j -= 1

            # 如果找到了，就放到左边的空位中，右边留出一个空位
            if i < j:
                lst[i] = lst[j]
                i += 1

            # 从左边找出一个比pivot大的数
            while i < j and lst[i] < pivot:
                i += 1

            # 如果找到了，就放到左边的空位中，右边留出一个空位
            if i < j:
                lst[j] = lst[i]
                j -= 1
        # 一直重复，直到i=j，将最先取出的i放回去
        print(i)
        lst[i] = pivot
        # 执行递归,因为i左边的都比i小，右边都不小于i，可以不使用i位置的元素了
        self.qsort_rec(lst, left, i - 1)
        self.qsort_rec(lst, i + 1, right)

        return lst


if __name__ == '__main__':
    # example = [30, 13, 25, 16, 47, 26, 19, 10]
    example = [5, 1, 3, 7]
    s = Solution()
    res = s.quick_sort(example)
    print(res)  # [10, 13, 16, 19, 25, 26, 30, 47]
