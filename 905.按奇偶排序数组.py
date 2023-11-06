#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#
# https://leetcode-cn.com/problems/sort-array-by-parity/description/
#
# algorithms
# Easy (68.04%)
# Likes:    129
# Dislikes: 0
# Total Accepted:    29.9K
# Total Submissions: 43.8K
# Testcase Example:  '[3,1,2,4]'
#
# 给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。
# 
# 你可以返回满足此条件的任何数组作为答案。
# 
# 
# 
# 示例：
# 
# 输入：[3,1,2,4]
# 输出：[2,4,3,1]
# 输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
# 
# 
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd, even = [], []
        for num in A:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even + odd
        
# @lc code=end

