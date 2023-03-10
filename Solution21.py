# Definition for singly-linked list
class ListNode:
    def __init__(self, val = 0, next = None):
       self.val = val
       self.next = next



class Solution21:

    def mergeTwoLists(self, list1 , list2):

        res = head = ListNode(0) # ListNode 是一个 class


        # 当 list1 和 list2 都不是 empty 的时候
        while list1 and list2:

            # .val 是 当前 value
            if list1.val < list2.val:
                head.next = list1 # 把一整个拼 过去？？？
                list1 = list1.next # pointer 跳转到下一个

            else:
                head.next = list2
                list2 = list2.next # pointer 跳转到下一下

            head = head.next # 继续拼接


        # if list1 is empty ---> 放到末尾
        if list1:
            head.next = list1

        # if list2 is empty ---> 放到末尾
        if list2:
            head.next = list2


        #### ?? 没有太明白 res ？？？？ 突然这么用
        return res.next # res 是头节点， res.next 便只向首节点，记录下head指向的首节点的地址



if __name__ == '__main__':

    # x 是 solution class的一个实例
    x = Solution21()

    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(4)
    n1.next = n2
    n2.next = n3

    print (n1)

    n11 = ListNode(1)
    n22 = ListNode(3)
    n33 = ListNode(4)
    n11.next = n22
    n22.next = n33


    #result = x.mergeTwoLists(n1,n11)
    #print(result)















