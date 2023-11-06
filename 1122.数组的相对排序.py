#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#
# https://leetcode-cn.com/problems/relative-sort-array/description/
#
# algorithms
# Easy (65.00%)
# Likes:    31
# Dislikes: 0
# Total Accepted:    10.2K
# Total Submissions: 15.7K
# Testcase Example:  '[2,3,1,3,2,4,6,7,9,2,19]\n[2,1,4,3,9,6]'
#
# 给你两个数组，arr1 和 arr2，
# 
# 
# arr2 中的元素各不相同
# arr2 中的每个元素都出现在 arr1 中
# 
# 
# 对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1
# 的末尾。
# 
# 
# 
# 示例：
# 
# 输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# 输出：[2,2,2,1,4,3,3,9,6,7,19]
# 
# 
# 
# 
# 提示：
# 
# 
# arr1.length, arr2.length <= 1000
# 0 <= arr1[i], arr2[i] <= 1000
# arr2 中的元素 arr2[i] 各不相同
# arr2 中的每个元素 arr2[i] 都出现在 arr1 中
# 
# 
#

# @lc code=start
from typing import List
class Solution:
    # 计数排序
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = [0] * (max(arr1) + 1)
        ans = []
        for num in arr1:
            arr[num] += 1
        for i in range(len(arr2)):
            while arr[arr2[i]] > 0:
                ans.append(arr2[i])
                arr[arr2[i]] -= 1
        for j in range(len(arr)):
            while arr[j] > 0:
                ans.append(j)
                arr[j] -= 1
        return ans

    # def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    #     tmp = 0
    #     for i in range(len(arr2)):
    #         for j in range(len(arr1)):
    #             if arr1[j] == arr2[i]:
    #                 arr1[j], arr1[tmp] = arr1[tmp], arr1[j]
    #                 tmp += 1
    #     arr1[tmp:] = sorted(arr1[tmp:])
    #     return arr1

                    

# @lc code=end

