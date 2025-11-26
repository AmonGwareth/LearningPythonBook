
class ListNode:

    def __init__(self, val, next_):
        self.val = val
        self.next = next_


class Solution:

    def __init__(self):
        self.running = True
        self.list_node = ListNode(0,None)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        while self.running:

            if (l1.val + l2.val) < 10:
                self.list_node.val = l1.val + l2.val
