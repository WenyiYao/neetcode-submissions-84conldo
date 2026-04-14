class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxNum = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                x = j - i
                y = min(heights[i], heights[j])
                value =  x * y
                if maxNum < value:
                    maxNum = value
        return maxNum
        