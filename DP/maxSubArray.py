# -*- coding: utf-8 -*-
"""
@Time : 2020/10/22 22:28
@Auth : Qi
@IDE  : PyCharm
@TiTle: 53. 最大子序和
@Link : https://leetcode-cn.com/problems/maximum-subarray/
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        ret = nums[0]
        pre = 0
        for value in nums:
            pre = max(pre + value, value)
            ret = max(pre, ret)
        return ret


if __name__ == '__main__':
    # 用例
    s = Solution()
    print(s.maxSubArray([-1, 1, 5, -6, 5, 9, 1]))
