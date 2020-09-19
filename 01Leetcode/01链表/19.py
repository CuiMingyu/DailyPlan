class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def removeNthFromEnd(head, n) -> ListNode:
    fast = ListNode(0)
    slow = ListNode(0)
    root = head

    while n > 0:
        head = head.next
        n -= 1

    fast = head
    slow = root

    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next

    return root
