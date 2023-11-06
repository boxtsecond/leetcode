#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#
# https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (48.73%)
# Likes:    95
# Dislikes: 0
# Total Accepted:    25.2K
# Total Submissions: 51.5K
# Testcase Example:  '["2","1","+","3","*"]'
#
# 根据逆波兰表示法，求表达式的值。
# 
# 有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
# 
# 说明：
# 
# 
# 整数除法只保留整数部分。
# 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
# 
# 
# 示例 1：
# 
# 输入: ["2", "1", "+", "3", "*"]
# 输出: 9
# 解释: ((2 + 1) * 3) = 9
# 
# 
# 示例 2：
# 
# 输入: ["4", "13", "5", "/", "+"]
# 输出: 6
# 解释: (4 + (13 / 5)) = 6
# 
# 
# 示例 3：
# 
# 输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# 输出: 22
# 解释: 
# ⁠ ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 
#

# @lc code=start
class Solution:
    # 链式栈
    # def evalRPN(self, tokens: List[str]) -> int:
    #     stack = LinkedStack()
    #     for x in tokens:
    #         if x not in '+-*/':
    #             stack.push(x)
    #         else:
    #             second_num = stack.pop()
    #             first_num = stack.pop()
    #             if first_num is not None and second_num is not None:
    #                 if x == '+':
    #                     stack.push(first_num + second_num)
    #                 elif x == '-':
    #                     stack.push(first_num - second_num)
    #                 elif x == '*':
    #                     stack.push(first_num * second_num)
    #                 elif x == '/':
    #                     stack.push(int(first_num / second_num))
    #                 else:
    #                     raise ValueError('expression error')
        
    #     return stack.pop()

    # 顺序栈
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for x in tokens:
            if x not in '+-*/':
                stack.append(int(x))
            else:
                second_num = stack.pop()
                first_num = stack.pop()
                if first_num is not None and second_num is not None:
                    if x == '+':
                        stack.append(first_num + second_num)
                    elif x == '-':
                        stack.append(first_num - second_num)
                    elif x == '*':
                        stack.append(first_num * second_num)
                    elif x == '/':
                        stack.append(int(first_num / second_num))
                    else:
                        raise ValueError('expression error')
        
        return stack[0]

class Node:
    def __init__(self, data):
        self.data = int(data)
        self.next: Node = None

# 链式栈
class LinkedStack:
    def __init__(self):
        self.top: Node = None
    
    def push(self, data) -> None:
        node = Node(data)
        if not self.top:
            self.top = node
        else:
            node.next = self.top
            self.top = node
    
    def pop(self):
        if not self.top:
            return None
        data = self.top.data
        self.top = self.top.next
        return data



# @lc code=end

