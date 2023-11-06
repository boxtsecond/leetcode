#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#
# https://leetcode-cn.com/problems/implement-queue-using-stacks/description/
#
# algorithms
# Easy (62.28%)
# Likes:    131
# Dislikes: 0
# Total Accepted:    30.8K
# Total Submissions: 49.3K
# Testcase Example:  '["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# 使用栈实现队列的下列操作：
# 
# 
# push(x) -- 将一个元素放入队列的尾部。
# pop() -- 从队列首部移除元素。
# peek() -- 返回队列首部的元素。
# empty() -- 返回队列是否为空。
# 
# 
# 示例:
# 
# MyQueue queue = new MyQueue();
# 
# queue.push(1);
# queue.push(2);  
# queue.peek();  // 返回 1
# queue.pop();   // 返回 1
# queue.empty(); // 返回 false
# 
# 说明:
# 
# 
# 你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty
# 操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
# 假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
# 
# 
#

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = Stack()
        self.pop_stack = Stack()
        
    # 时间复杂度 O(1), 空间复杂度 O(n)
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.push_stack.push(x)
        
    # 均摊时间复杂度 O(1), 空间复杂度 O(1)
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return
            
        if self.pop_stack.empty():
            pop_data = self.push_stack.pop()
            while pop_data:
                self.pop_stack.push(pop_data)
                pop_data = self.push_stack.pop()
        
        return self.pop_stack.pop()
        
    # 时间复杂度 O(1), 空间复杂度 O(1)
    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.push_stack.empty():
            return self.push_stack.stack[0]
        elif not self.pop_stack.empty():
            return self.pop_stack.stack[-1]
    
    # 时间复杂度 O(1), 空间复杂度 O(1)
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.push_stack.empty() and self.pop_stack.empty()
        
class Stack:
    def __init__(self):
        self.stack = []
    
    def pop(self) -> int:
        if len(self.stack):
            return self.stack.pop()

    def push(self, data: int):
        self.stack.append(data)

    def empty(self) -> bool:
        return not len(self.stack)
    



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

