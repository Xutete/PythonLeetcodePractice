class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution17_Nth_from_end:
    def removeNthFromEnd(self, head, n):
        head_dummy = ListNode()
        head_dummy.next = head

        slow, fast = head_dummy, head_dummy
        while(n != 0): # fast 先往前走n步
            fast = fast.next
            n -= 1

        while(fast.next != None):
            slow = slow.next
            fast = fast.next


        # fast 走到结尾后，slow的下一个节点为倒数第N个节点

        slow.next = slow.next.next # 删除操作！！！

        return head_dummy.next












