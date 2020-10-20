# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/20 20:44
@Auth ： Qi
@IDE ：PyCharm
"""
from leetcode.ListNode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return
        lastList = None
        midList = head
        nextList = midList.next
        while midList.next is not None:
            midList.next = lastList
            lastList = midList
            midList = nextList
            nextList = midList.next
        midList.next = lastList
        return midList


if __name__ == "__main__":
    # 测试用例
    # 新建一个链表
    newList = ListNode.create([0, 1, 2, 3, 4])

    # 输出原先的链表
    print(ListNode.toList(newList))
    # 反转链表
    newList = Solution().reverseList(newList)
    # 输出新的链表
    print(ListNode.toList(newList))
