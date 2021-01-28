class Solution:
    def insertion_sort(self, lst):
        n = len(lst)
        # 第一个元素默认是有序的，因为是逐个取下一个元素，所以需要到n
        for i in range(1, n):
            # 要插入的元素
            tmp = lst[i]
            j = i
            # 一直比较到第0个元素，且用到j-1, 所以循环的条件是j > 0.否则超过索引
            while j > 0 and lst[j-1] > tmp:
                # 前一个元素后移一个位置
                lst[j] = lst[j-1]
                j -= 1
            # j即是要插入的位置，将数据插入到该位置
            lst[j] = tmp
        return lst




if __name__ == '__main__':
    example = [49, 38, 65, 97, 76, 13, 27, 49, 55, 4]
    s = Solution()
    res = s.insertion_sort(example)
    print(res)  # [4, 13, 27, 38, 49, 49, 55, 65, 76, 97]
