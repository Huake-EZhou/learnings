class Solution:
    def shell_sort(self, lst):
        n = len(lst)
        gap = n // 2
        # gap //= 2一直重复的结果是0，所以循环的条件是gap > 0
        while gap > 0:
            # 从gap开始，每组交叉比较
            for i in range(gap, n):
                # 插入排序
                tmp = lst[i]
                j = i
                while j > 0 and lst[j-gap] > tmp:  # 同组前一个元素是j-gap
                    # 前一个元素后移一个位置
                    lst[j] = lst[j-gap]
                    # 索引指针前移一个位置
                    j -= gap
                # 同组元素有可能后移了，也有可能没有后移，所以最前面的一个元素都要重新赋值一遍
                lst[j] = tmp
            gap //= 2
        return lst


if __name__ == '__main__':
    example = [49, 38, 65, 97, 76, 13, 27, 49, 55, 4]
    s = Solution()
    res = s.shell_sort(example)
    print(res)  # [4, 13, 27, 38, 49, 49, 55, 65, 76, 97]
