#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#
# https://leetcode-cn.com/problems/implement-stack-using-queues/description/
#
# algorithms
# Easy (61.96%)
# Likes:    113
# Dislikes: 0
# Total Accepted:    28.5K
# Total Submissions: 45.8K
# Testcase Example:  '["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# 使用队列实现栈的下列操作：
# 
# 
# push(x) -- 元素 x 入栈
# pop() -- 移除栈顶元素
# top() -- 获取栈顶元素
# empty() -- 返回栈是否为空
# 
# 
# 注意:
# 
# 
# 你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty
# 这些操作是合法的。
# 你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
# 你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
# 
# 
#

# @lc code=start
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_queue = Queue()
        self.pop_queue = Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.push_queue.enqueue(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return
        
        if self.pop_queue.empty():
            while self.push_queue.size() > 1:
                self.pop_queue.enqueue(self.push_queue.dequeue())
        tmp = self.push_queue
        self.push_queue = self.pop_queue
        self.pop_queue = tmp
        return self.pop_queue.dequeue()

    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.push_queue.empty():
            return self.push_queue.queue[-1]
        elif not self.pop_queue.empty():
            return self.pop_queue.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.push_queue.empty() and self.pop_queue.empty()

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data: int) -> None:
        self.queue.append(data)

    def dequeue(self) -> int:
        if not self.empty():
            data = self.queue[0]
            self.queue.pop(0)
            return data
    
    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not len(self.queue)
    
    def size(self) -> int:
        return len(self.queue)



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

