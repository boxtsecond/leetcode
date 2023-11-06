#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.66%)
# Likes:    1363
# Dislikes: 0
# Total Accepted:    195.5K
# Total Submissions: 480.2K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        stack = LinkedStack()
        for i in s:
            if i == '{' or i == '[' or i == '(':
                stack.push(i)
            else:
                p = stack.pop()
                if not p:
                    return False
                if p == '{' and i != '}':
                    return False
                if p == '[' and i != ']':
                    return False
                if p == '(' and i != ')':
                    return False

        return not stack.top

class Node:
    def __init__(self, data: str):
        self.data = data
        self.next = None

# 链式栈
class LinkedStack:
    def __init__(self):
        self.top :Node = None

    def push(self, data: str) -> None:
        node = Node(data)
        if not self.top:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self) -> str:
        if not self.top:
            return ''

        data = self.top.data
        self.top = self.top.next
        return data


# @lc code=end

