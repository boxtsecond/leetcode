#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (39.03%)
# Likes:    3386
# Dislikes: 0
# Total Accepted:    286K
# Total Submissions: 732.7K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
# 
# 进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
# 
# 
# 
# 示例 1：
# 
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
# 
# 
# 示例 2：
# 
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
# 
# 
# 示例 3：
# 
# 输入：nums1 = [0,0], nums2 = [0,0]
# 输出：0.00000
# 
# 
# 示例 4：
# 
# 输入：nums1 = [], nums2 = [1]
# 输出：1.00000
# 
# 
# 示例 5：
# 
# 输入：nums1 = [2], nums2 = []
# 输出：2.00000
# 
# 
# 
# 
# 提示：
# 
# 
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n, count, i, j = len(nums1), len(nums2), 0, 0, 0
        if m == 0:
            return (nums2[int(n/2)] + nums2[int((n-1)/2)]) / 2
        if n == 0:
            return (nums1[int(m/2)] + nums1[int((m-1)/2)]) / 2

        result = []
        while count <= (m + n) // 2:
            num = None
            if i == m:
                num = nums2[j]
                j += 1
            elif j == n:
                num = nums1[i]
                i += 1
            elif nums1[i] < nums2[j]:
                if i != m:
                    num = nums1[i]
                    i += 1
                else:
                    num = nums2[j]
                    j += 1
            else:
                if j != n:
                    num = nums2[j]
                    j += 1
                else:
                    num = nums1[i]
                    i += 1
            if count >= (m + n) // 2 - 1:
                result.append(num)
            count += 1

        if (m + n) % 2 == 0:
            return (result[0] + result[1]) / 2
        else:
            return result[1] 

# @lc code=end

