#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#
# https://leetcode-cn.com/problems/backspace-string-compare/description/
#
# algorithms
# Easy (49.89%)
# Likes:    86
# Dislikes: 0
# Total Accepted:    14.4K
# Total Submissions: 28.7K
# Testcase Example:  '"ab#c"\n"ad#c"'
#
# 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
# 
# 
# 
# 示例 1：
# 
# 输入：S = "ab#c", T = "ad#c"
# 输出：true
# 解释：S 和 T 都会变成 “ac”。
# 
# 
# 示例 2：
# 
# 输入：S = "ab##", T = "c#d#"
# 输出：true
# 解释：S 和 T 都会变成 “”。
# 
# 
# 示例 3：
# 
# 输入：S = "a##c", T = "#a#c"
# 输出：true
# 解释：S 和 T 都会变成 “c”。
# 
# 
# 示例 4：
# 
# 输入：S = "a#c", T = "b"
# 输出：false
# 解释：S 会变成 “c”，但 T 仍然是 “b”。
# 
# 
# 
# 提示：
# 
# 
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S 和 T 只含有小写字母以及字符 '#'。
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_result = self.getResult(S)
        t_result = self.getResult(T)
        return s_result == t_result

    def getResult(self, S: str) -> list:
        stack = SequenceStack()
        for x in S:
            if x != '#':
                stack.push(x)
            else:
                stack.pop()
        return stack.stack


class SequenceStack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack):
            self.stack.pop()
    
    def push(self, data: str):
        self.stack.append(data)




        
# @lc code=end

