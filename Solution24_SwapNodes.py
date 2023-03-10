class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#

class Solution24_SwapNodes:
    def swapPairs(self, head):

        head_dummy = ListNode()
        head_dummy.next = head

        # prev_node
        prev_node = head_dummy

        while head != None and head.next != None:

            # Nodes to be swapped
            first_node = head
            second_node = head.next

            # swapping
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next

        return head_dummy.next














