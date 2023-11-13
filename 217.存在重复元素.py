#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#
# https://leetcode.cn/problems/contains-duplicate/description/
#
# algorithms
# Easy (54.98%)
# Likes:    1059
# Dislikes: 0
# Total Accepted:    827.9K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3,1]'
#
# 给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3,1]
# 输出：true
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3,4]
# 输出：false
# 
# 示例 3：
# 
# 
# 输入：nums = [1,1,1,3,3,4,3,2,4,2]
# 输出：true
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def containsDuplicate_1(self, nums: List[int]) -> bool:
        kv = {}
        for each in nums:
            if each in kv:
                return True
            kv[each] = True
        return False
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    
# @lc code=end

