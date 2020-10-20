"""
Author : Qi
Date : 2020/10/20
Link : https://leetcode-cn.com/problems/reorder-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
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
    # 下面是测试用例

    # 构建链表
    p = q = ListNode(0)
    for i in range(5):
        q.next = ListNode(i + 1)
        q = q.next
    # 输出转换之前链表
    q = p
    print(q.val, '     ', id(q))
    while q.next is not None:
        q = q.next
        print(q.val, '     ', id(q))
    # 进行转换
    Solution().reorderList(p)
    print('--------------------')
    # 输出转换之后列表
    q = p
    print(q.val, '     ', id(q))
    while q.next is not None:
        q = q.next
        print(q.val, '     ', id(q))
