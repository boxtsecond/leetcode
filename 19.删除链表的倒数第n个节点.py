#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head

        while n != 0 and fast:
            fast = fast.next
            n -= 1

        if n != 0 or not fast:
            head = head.next
            return head
        
        while fast.next:
            fast = fast.next
            slow = slow.next  

        slow.next = slow.next.next
        return head

            
        

            
        
# @lc code=end

