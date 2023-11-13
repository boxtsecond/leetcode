#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
# https://leetcode.cn/problems/move-zeroes/description/
#
# algorithms
# Easy (63.57%)
# Likes:    2222
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 1.9M
# Testcase Example:  '[0,1,0,3,12]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 
# 
# 示例 2:
# 
# 
# 输入: nums = [0]
# 输出: [0]
# 
# 
# 
# 提示:
# 
# 
# 
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# 
# 
# 
# 
# 进阶：你能尽量减少完成的操作次数吗？
# 
#
from typing import List
# @lc code=start
class Solution:
    def moveZeroes_1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. 0 放入数组最后
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] == 0:
                while i < j and nums[j] == 0:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            i += 1

        while j > 0 and nums[j] == 0:
            j -= 1
       #  print(nums, i, j)
        if j <= 0:
            return
        
        # 2. 非 0 排序, [0,j]
        # mistake: 还以为要排序
        self.quickSort(nums, 0, j)
    
    def quickSort(self, nums: List[int], start, end: int) -> None:
        if start >= end:
            return
         
        p, i, j = start, start+1, end
        while i <= j:
            if nums[i] < nums[p]:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
            i += 1

        self.quickSort(nums, 0, p-1)
        self.quickSort(nums, p+1, end)

    def moveZeroes_2(self, nums: List[int]) -> None:
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                i = j
                while i < len(nums) and nums[i] == 0:
                    i += 1
                if i == len(nums):
                    return
                nums[i], nums[j] = nums[j], nums[i]
            j += 1

    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        # 1,3,0,0,12
        for i in range(len(nums)):
            if nums[i]:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1


# @lc code=end

