class Solution:
    def selection_sort(self, lst):
        # 序列长度
        n = len(lst)
        # 只需要遍历n-1遍即可，余下的最后一个元素不用比较
        for i in range(n - 1):
            # 与未排序序列比较(i+1的关系)，选择出最小元素的索引
            min_index = i
            # 最后一个元素也是要比较的，所以要遍历到n
            for j in range(i + 1, n):
                if lst[j] < lst[min_index]:
                    min_index = j
            # 如果第i个位置的元素不是最小的元素，那么则两两交换
            if i != min_index:
                lst[i], lst[min_index] = lst[min_index], lst[i]
        return lst


if __name__ == '__main__':
    example = [30, 13, 25, 16, 47, 26, 19, 10]
    s = Solution()
    res = s.selection_sort(example)
    print(res)  # [10, 13, 16, 19, 25, 26, 30, 47]
