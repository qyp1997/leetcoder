# -*- coding: utf-8 -*-
"""
@Time : 2020/10/21 9:38
@Auth : Qi
@IDE  : PyCharm
@Title: 925. 长按键入
@Link : https://leetcode-cn.com/problems/long-pressed-name/
"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j <= 0 or typed[j] != typed[j - 1]:
                return False
            else:
                j += 1
        return True if i >= len(name) else False


if __name__ == "__main__":
    # 测试用例
    s = Solution()
    print(s.isLongPressedName('alex', 'ffefesf'))
    print(s.isLongPressedName('bob', 'bobwafa'))
    print(s.isLongPressedName('bob', 'bobbbbbbbbb'))
