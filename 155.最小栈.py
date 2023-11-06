#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
# https://leetcode-cn.com/problems/min-stack/description/
#
# algorithms
# Easy (51.11%)
# Likes:    368
# Dislikes: 0
# Total Accepted:    69.4K
# Total Submissions: 135.4K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
# 
# 
# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。
# 
# 
# 示例:
# 
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
# 
# 
#

# @lc code=start

# 链表栈，使用链表实现
# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.t: Node = None
#         self.min: Node = None
        
#     def push(self, x: int) -> None:
#         node = Node(x)
#         min_node = Node(x)
#         if not self.t:
#             self.t = node
#             self.min = node
#         else:
#             node.next = self.t
#             self.t = node
#             if node.data <= self.min.data:
#                 min_node.next = self.min
#                 self.min = min_node
        
#     def pop(self) -> None:
#         if self.t:
#             if self.t.data == self.min.data:
#                 self.min = self.min.next
#             self.t = self.t.next 

#     def top(self) -> int:
#         return self.t and self.t.data

#     def getMin(self) -> int:
#         return self.min and self.min.data

# 顺序栈，使用数组实现   
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.t = []
        self.min = []
        
    def push(self, x: int) -> None:
        self.t.append(x)
        if not len(self.min):
            self.min.append(x)
        elif x <= self.min[-1]:
            self.min.append(x)
        
    def pop(self) -> None:
        x = self.t.pop()
        if len(self.min) and x == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        if len(self.t):
            return self.t[-1]

    def getMin(self) -> int:
        if len(self.min):
            return self.min[-1]


# class Node:
#     def __init__(self, data: int):
#         self.data = data
#         self.next = None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

