# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def create(li: list):
        """
        新建一个链表
        :param li: 链表的值
        :return: 头节点
        """
        if len(li) == 0:
            return None
        ret = tmp = ListNode(li[0])
        for i in li[1:]:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return ret

    @staticmethod
    def toList(head) -> list:
        """
        链表转换到列表
        :param head:头节点
        :return:列表
        """
        li = []
        p1 = head
        while p1:
            li.append(p1.val)
            p1 = p1.next
        return li