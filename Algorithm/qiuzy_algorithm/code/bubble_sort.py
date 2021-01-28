class Solution:
    def bubble_sort(self, lst):
        n = len(lst)
        # 每次都是从第0个元素开始
        for i in range(n-1):
            # 前面一个指针从1开始，每做1遍，就减少1项
            for j in range(1, n-i):
                # 相邻元素比较，如果是逆序就交换
                if lst[j-1] > lst[j]:
                    lst[j-1], lst[j] = lst[j], lst[j-1]
        return lst


if __name__ == '__main__':
    example = [30, 13, 25, 16, 47, 26, 19, 10]
    s = Solution()
    res = s.bubble_sort(example)
    print(res)  # [10, 13, 16, 19, 25, 26, 30, 47]

