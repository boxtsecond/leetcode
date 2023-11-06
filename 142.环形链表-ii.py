#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#
# https://leetcode-cn.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (47.80%)
# Likes:    348
# Dislikes: 0
# Total Accepted:    47.8K
# Total Submissions: 100K
# Testcase Example:  '[3,2,0,-4]\n1'
#
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# 
# 说明：不允许修改给定的链表。
# 
# 
# 
# 示例 1：
# 
# 输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 
# 
# 
# 
# 示例 2：
# 
# 输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
# 
# 
# 
# 
# 示例 3：
# 
# 输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。
# 
# 
# 
# 
# 
# 
# 进阶：
# 你是否可以不用额外空间解决此题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 使用set，时间复杂度 O(n)，空间复杂度 O(n)
    # def detectCycle(self, head: ListNode) -> ListNode:
    #     if not head or not head.next:
    #         return 
        
    #     node_set = set()
    #     node = head
    #     while node:
    #         if node in node_set:
    #             return node
    #         else:
    #             node_set.add(node)
    #             node = node.next

    '''
    快慢指针相遇法，时间复杂度 O(n)，空间复杂度 O(1)
    1. 使用快慢指针，找到相遇点
    2. 两指针分别从从头结点、相遇点出发，再次相遇时则为入环点

    解析：
    先假设环的长度远大于入环点前的长度，便于理解
    1. 当慢指针走到入环点时，假设入环点前的长度为 n，快指针走完入环点前的路并且在环内走了n
    2. 假设环内剩余的长度为 r，r + n = 环长
    3. 此时快慢指针都在环内，当慢指针再走 r 的长度，则快指针走过 2r，再加上之前快指针的位置 n，则快指针在环 r 的位置，于是快慢指针在 r 相遇
    4. 相遇点距离入环点正好为 n，即入环点前的长度
    5. 当两个指针分别从头结点、相遇点同时出发，相遇时则为入环点
    当环的长度很小的时候，可以理解为将多个小环铺展开成一个大环，和上述情况一致
    '''
    def detectCycle(self, head: ListNode) -> ListNode:
        mnode = self.getMeetNode(head)
        if not mnode:
            return
        node = head
        while node:
            if mnode == node:
                return node
            node = node.next
            mnode = mnode.next
        return None

    def getMeetNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        if not head or not head.next:
            return head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return slow

# @lc code=end

