class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    root = n = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1 + v2 + carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next


n1 = ListNode(2)
n2 = ListNode(4)
n3 = ListNode(3)
n1.next = n2
n2.next = n3

n4 = ListNode(5)
n5 = ListNode(6)
n6 = ListNode(4)
n4.next = n5
n5.next = n6

addTwoNumbers(n1, n4)
