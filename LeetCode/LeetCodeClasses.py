# Add two numbers
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionEx2:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l3 = ListNode()

        if (l1.val + l2.val) < 10:
            l3.val = l1.val + l2.val
            # l3.next = ListNode()
        else:
            l3.val = (l1.val + l2.val) % 10


            # def add_values(l1, l2):
        #     return val1 + val2