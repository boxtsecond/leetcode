#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (66.65%)
# Likes:    750
# Dislikes: 0
# Total Accepted:    149.6K
# Total Submissions: 224.3K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 时间复杂度 O(n)，空间复杂度 O(n)
    # 由于使用递归，将会使用隐式栈空间。递归深度可能会达到 n 层，所以空间复杂度为 O(n)
    # def reverseList(self, head: ListNode) -> ListNode:
    #     if not head or not head.next:
    #         return head
    #     node = self.reverseList(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return node

    # 时间复杂度 O(n)，空间复杂度 O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        prev = head
        node = head.next
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        head.next = None
        head = prev
        return head

        
# @lc code=end

