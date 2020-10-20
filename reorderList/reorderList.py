# -*- coding: utf-8 -*-
"""
@Time : 2020/10/20 20:52
@Auth : Qi
@IDE  : PyCharm
@Link : https://leetcode-cn.com/problems/reorder-list/
"""
from leetcode.ListNode import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        重排列表
        :param head:
        :return:
        """
        if not head:
            return
        tempHead = head
        li = []
        while tempHead:
            li.append(tempHead)
            tempHead = tempHead.next

        x, y = 0, len(li) - 1
        while x < y:
            li[x].next = li[y]
            x += 1
            if x >= y:
                break
            li[y].next = li[x]
            y -= 1
        if x >= y:
            li[x].next = None


if __name__ == '__main__':
    # 测试用例

    # 构建链表
    newList = ListNode.create([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # 输出转换之前链表
    print(ListNode.toList(newList))
    # 进行转换
    Solution().reorderList(newList)
    # 输出转换之后列表
    print(ListNode.toList(newList))