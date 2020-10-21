# -*- coding: utf-8 -*-
"""
@Time : 2020/10/21 10:39
@Auth : Qi
@IDE  : PyCharm
@Title: 6. Z 字形变换
@Link : https://leetcode-cn.com/problems/zigzag-conversion/
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 0:
            return ''
        if numRows == 1:
            return s
        ret = ''
        for i in range(numRows):
            tmp = i
            time = numRows * 2 - 2
            while tmp < len(s):
                if i == 0 or i == numRows - 1 and tmp:
                    ret += s[tmp]
                    tmp += time
                else:
                    ret += s[tmp]
                    if tmp + time - i * 2 < len(s):
                        ret += s[tmp + time - i * 2]
                    else:
                        break
                    tmp += time
        return ret


if __name__ == '__main__':
    # 测试用例
    s = Solution()
    print(s.convert('ABCDE', 4))
