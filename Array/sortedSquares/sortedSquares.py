# -*- coding: utf-8 -*-
"""
@Time : 2020/10/25 17:38
@Auth : Qi
@IDE  : PyCharm
@Title: 977. 有序数组的平方
@Link : https://leetcode-cn.com/problems/squares-of-a-sorted-array/
"""


class Solution:
    def sortedSquares(self, A):
        ret = []
        for num in A:
            ret.append(num * num)
        return sorted(ret)

        # 备注内容采用二分查找法 每次添加到合适的位置
        # def insertSorted(li, n):
        #     if not li:
        #         li.append(n)
        #     else:
        #         left, right = 0, len(li) - 1
        #         while right - left >= 0:
        #             mid = (left + right) // 2
        #             if li[mid] == n:
        #                 left = mid
        #                 break
        #             elif li[mid] > n:
        #                 right = mid - 1
        #             else:
        #                 left = mid + 1
        #         li.insert(left, n)
        #
        # ret = []
        # for num in A:
        #     insertSorted(ret, num * num)
        # return ret


if __name__ == '__main__':
    # 测试用例
    s = Solution()
    print(s.sortedSquares([-4, -1, 0, 3, 10]))
    print(s.sortedSquares([-7, -3, 2, 3, 11]))
