#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#
# https://leetcode-cn.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (42.96%)
# Likes:    93
# Dislikes: 0
# Total Accepted:    24.2K
# Total Submissions: 55.8K
# Testcase Example:  '16'
#
# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
# 
# 说明：不要使用任何内置的库函数，如  sqrt。
# 
# 示例 1：
# 
# 输入：16
# 输出：True
# 
# 示例 2：
# 
# 输入：14
# 输出：False
# 
# 
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        low, high = 2, num // 2
        while low <= high:
            mid = low + ((high - low) >> 1)
            square = mid * mid
            if square == num:
                return True
            elif square > num:
                high = mid - 1
            else:
                low = mid + 1
        return False
        # 牛顿迭代法
        # x = num // 2
        # while x * x > num:
        #     x = (x + num // x) // 2
        # return x * x == num

            
            


# @lc code=end

