# -*- coding: utf-8 -*-
"""
@Time : 2020/10/25 17:14
@Auth : Qi
@IDE  : PyCharm
@Title: 845. 数组中的最长山脉
@Link : https://leetcode-cn.com/problems/longest-mountain-in-array/
"""


class Solution:
    def longestMountain(self, A) -> int:
        up, down, maxRet = 0, 0, 0
        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                if down > 0:  # if up > 0 and down > 0
                    maxRet = max(up + down + 1, maxRet)
                up, down = 0, 0
            elif A[i] > A[i - 1]:
                if down == 0:
                    up += 1
                else:
                    if down > 0:  # if up > 0 and down > 0
                        maxRet = max(up + down + 1, maxRet)
                    up, down = 1, 0
            elif up > 0:  # A[i]<A[i-1]
                down += 1
        return max(up + down + 1, maxRet) if up > 0 and down > 0 else maxRet


if __name__ == '__main__':
    # 测试用例
    s = Solution()
    print(s.longestMountain([2, 1, 4, 7, 3, 2, 5]))
    print(s.longestMountain([0, 1, 0, 0, 1, 1, 1, 1]))
    print(s.longestMountain([2, 2, 2]))
