#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#
# https://leetcode-cn.com/problems/peak-index-in-a-mountain-array/description/
#
# algorithms
# Easy (69.05%)
# Likes:    68
# Dislikes: 0
# Total Accepted:    20.1K
# Total Submissions: 28.9K
# Testcase Example:  '[0,1,0]'
#
# 我们把符合下列属性的数组 A 称作山脉：
# 
# 
# A.length >= 3
# 存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... >
# A[A.length - 1]
# 
# 
# 给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... >
# A[A.length - 1] 的 i 的值。
# 
# 
# 
# 示例 1：
# 
# 输入：[0,1,0]
# 输出：1
# 
# 
# 示例 2：
# 
# 输入：[0,2,1,0]
# 输出：1
# 
# 
# 
# 提示：
# 
# 
# 3 <= A.length <= 10000
# 0 <= A[i] <= 10^6
# A 是如上定义的山脉
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        low, high = 0, len(A) - 1
        while low < high:
            mid = low + ((high - low) >> 1)
            if A[mid] < A[mid + 1]:
                low = mid + 1
            else: 
                high = mid
        return low



        
# @lc code=end

