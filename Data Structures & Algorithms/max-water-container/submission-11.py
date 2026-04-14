class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxNum = 0
        left, right = 0, len(heights) - 1
        while left < right:
            x = right - left
            y = min(heights[left],heights[right])
            area = x * y
            if maxNum < area:
                maxNum = area
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxNum
        