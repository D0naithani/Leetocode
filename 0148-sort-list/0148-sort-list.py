from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Helper: Split the list into two halves
        def split(head):
            mid = prev = head
            while mid.next and mid.next.next:
                prev = mid
                mid = mid.next.next
            # Cut the list at prev
            second = prev.next
            prev.next = None
            return second

        # Helper: Merge two sorted lists
        def merge(l1, l2):
            dummy = ListNode(0)
            tail = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next, l1 = l1, l1.next
                else:
                    tail.next, l2 = l2, l2.next
                tail = tail.next
            tail.next = l1 or l2
            return dummy.next

        # Step 1: Find length
        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        # Step 2: Bottom-up merge sort
        length = get_length(head)
        dummy = ListNode(0, head)
        step = 1

        while step < length:
            prev = dummy
            curr = dummy.next
            while curr:
                # Split into two sublists of size 'step'
                first = curr
                second = self.get_sublist(first, step)
                curr = self.get_sublist(second, step)

                # Merge and reconnect
                merged = merge(first, second)
                prev.next = merged
                while prev.next:
                    prev = prev.next
            step *= 2

        return dummy.next

    # Helper: Split the list starting from 'node' with given 'step'
    def get_sublist(self, node, step):
        for _ in range(step - 1):
            if node and node.next:
                node = node.next
        if not node:
            return None
        second = node.next
        node.next = None  # Cut off sublist
        return second