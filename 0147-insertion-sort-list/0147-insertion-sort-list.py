class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        curr = head.next
        last_sorted = head

        while curr:
            if last_sorted.val <= curr.val:
                # No need to remove; already in order
                last_sorted = last_sorted.next
            else:
                # Start from beginning to find insertion point
                prev = dummy
                while prev.next.val <= curr.val:
                    prev = prev.next
                # Remove current node
                last_sorted.next = curr.next
                # Insert curr after prev
                curr.next = prev.next
                prev.next = curr
            curr = last_sorted.next

        return dummy.next