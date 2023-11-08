#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
# https://leetcode.cn/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (68.92%)
# Likes:    518
# Dislikes: 0
# Total Accepted:    288.3K
# Total Submissions: 418.4K
# Testcase Example:  '3'
#
# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
# 
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
# 
# 
# 
# 
# 
# 示例 1:
# 
# 
# 输入: rowIndex = 3
# 输出: [1,3,3,1]
# 
# 
# 示例 2:
# 
# 
# 输入: rowIndex = 0
# 输出: [1]
# 
# 
# 示例 3:
# 
# 
# 输入: rowIndex = 1
# 输出: [1,1]
# 
# 
# 
# 
# 提示:
# 
# 
# 0 
# 
# 
# 
# 
# 进阶：
# 
# 你可以优化你的算法到 O(rowIndex) 空间复杂度吗？
# 
#
# @lc code=start
class Solution:
    def getRow_1(self, rowIndex: int) -> List[int]:
        base = [[1],[1,1]]
        if rowIndex < 2:
            return base[rowIndex]
        
        prev = []
        while rowIndex > 0:
            row = [1]
            last = prev
            for i in range(1, len(last)):
                row.append(last[i - 1] + last[i])
            row.append(1)
            prev = row
            rowIndex -= 1
        return prev
    
    def getRow(self, rowIndex: int) -> List[int]:
        base = [[1],[1,1]]
        if rowIndex < 2:
            return base[rowIndex]
        
        row = [1]
        for i in range(1, rowIndex+1):
            row.append(int(row[i - 1] * (rowIndex - i + 1) / i))
        return row


# @lc code=end

