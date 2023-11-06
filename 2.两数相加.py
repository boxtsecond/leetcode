#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (38.86%)
# Likes:    5228
# Dislikes: 0
# Total Accepted:    618.1K
# Total Submissions: 1.6M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 
# 示例：
# 
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        current = result
        carry = 0
        while l1 or l2:
            r = 0 
            if l1:
                r += l1.val
            if l2:
                r += l2.val
            if carry:
                r += carry
                carry = 0
            if r > 9:
                r = r % 10
                carry = 1    
            current.next = ListNode(r)
            current = current.next
            l1 = l1 and l1.next
            l2 = l2 and l2.next
        if carry:
            current.next = ListNode(carry)

        return result.next    

# @lc code=end

