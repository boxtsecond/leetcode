#
# @lc app=leetcode.cn id=622 lang=python3
#
# [622] 设计循环队列
#
# https://leetcode-cn.com/problems/design-circular-queue/description/
#
# algorithms
# Medium (39.77%)
# Likes:    78
# Dislikes: 0
# Total Accepted:    20.1K
# Total Submissions: 50.3K
# Testcase Example:  '["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]\n[[3],[1],[2],[3],[4],[],[],[],[4],[]]'
#
# 设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于
# FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。
# 
# 
# 循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。
# 
# 你的实现应该支持如下操作：
# 
# 
# MyCircularQueue(k): 构造器，设置队列长度为 k 。
# Front: 从队首获取元素。如果队列为空，返回 -1 。
# Rear: 获取队尾元素。如果队列为空，返回 -1 。
# enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
# deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
# isEmpty(): 检查循环队列是否为空。
# isFull(): 检查循环队列是否已满。
# 
# 
# 
# 
# 示例：
# 
# MyCircularQueue circularQueue = new MycircularQueue(3); // 设置长度为 3
# 
# circularQueue.enQueue(1);  // 返回 true
# 
# circularQueue.enQueue(2);  // 返回 true
# 
# circularQueue.enQueue(3);  // 返回 true
# 
# circularQueue.enQueue(4);  // 返回 false，队列已满
# 
# circularQueue.Rear();  // 返回 3
# 
# circularQueue.isFull();  // 返回 true
# 
# circularQueue.deQueue();  // 返回 true
# 
# circularQueue.enQueue(4);  // 返回 true
# 
# circularQueue.Rear();  // 返回 4
# 
# 
# 
# 
# 提示：
# 
# 
# 所有的值都在 0 至 1000 的范围内；
# 操作数将在 1 至 1000 的范围内；
# 请不要使用内置的队列库。
# 
# 
#

# @lc code=start

# 使用数组实现
# class MyCircularQueue:

#     def __init__(self, k: int):
#         """
#         Initialize your data structure here. Set the size of the queue to be k.
#         """
#         # Tail = (Head + Count - 1) % Limit
#         self.queue = [0] * k
#         self.limit = k
#         self.head = 0
#         self.count = 0

#     def enQueue(self, value: int) -> bool:
#         """
#         Insert an element into the circular queue. Return true if the operation is successful.
#         """
#         if self.isFull():
#             return False
        
#         self.queue[(self.head + self.count) % self.limit] = value
#         self.count += 1
#         return True

#     def deQueue(self) -> bool:
#         """
#         Delete an element from the circular queue. Return true if the operation is successful.
#         """
#         if self.isEmpty():
#             return False

#         self.head = (self.head + 1) % self.limit
#         self.count -= 1
#         return True

#     def Front(self) -> int:
#         """
#         Get the front item from the queue.
#         """
#         if self.isEmpty():
#             return -1
#         return self.queue[self.head]

#     def Rear(self) -> int:
#         """
#         Get the last item from the queue.
#         """
#         if self.isEmpty():
#             return -1
#         tail = (self.head + self.count - 1) % self.limit
#         return self.queue[tail]

#     def isEmpty(self) -> bool:
#         """
#         Checks whether the circular queue is empty or not.
#         """
#         return self.count == 0

#     def isFull(self) -> bool:
#         """
#         Checks whether the circular queue is full or not.
#         """
#         return self.count == self.limit

# 使用链表实现
class Node:
    def __init__(self, data: int, nextNode = None):
        self.data = data
        self.next = nextNode

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.limit = k
        self.head: Node = None
        self.tail: Node = None
        self.count = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            node = Node(value)
            self.tail.next = node
            self.tail = node
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
        self.head = self.head.next
        self.count -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.head.data
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.tail.data

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.limit


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end

