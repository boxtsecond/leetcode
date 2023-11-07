#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# https://leetcode.cn/problems/plus-one/description/
#
# algorithms
# Easy (45.24%)
# Likes:    1316
# Dislikes: 0
# Total Accepted:    680.2K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3]'
#
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
# 
# 
# 示例 2：
# 
# 
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
# 
# 
# 示例 3：
# 
# 
# 输入：digits = [0]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def plusOne_1(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] + 1 < 10:
                digits[i] = digits[i] + 1
                break
            digits[i] = 0
            i -= 1 
        if digits[0] == 0:
            digits = [1] + digits
        return digits
    
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            digits[i] += 1
            digits[i] = digits[i] % 10
            if digits[i] != 0:
                break
            i -= 1 

        if digits[0] == 0:
            digits = [1] + digits
        return digits

# @lc code=end

