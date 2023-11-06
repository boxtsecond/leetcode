#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (38.73%)
# Likes:    328
# Dislikes: 0
# Total Accepted:    66.1K
# Total Submissions: 169.2K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 
# 你的算法时间复杂度必须是 O(log n) 级别。
# 
# 如果数组中不存在目标值，返回 [-1, -1]。
# 
# 示例 1:
# 
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 
# 示例 2:
# 
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
# 
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if length == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        first = self.findLeft(length, nums, target)
        end = self.findRight(length, nums, target)
        
        return [first, end]
    
    def findLeft(self, length: int, nums: List[int], target: int):
        low, high = 0, length - 1 
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                else:
                    high = mid - 1
        return -1

    def findRight(self, length: int, nums: List[int], target: int):
        low, high = 0, length - 1 
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                if mid == length - 1 or nums[mid + 1] > target:
                    return mid
                else:
                    low = mid + 1
        return -1




# @lc code=end

