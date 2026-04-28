class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_result = 0

        while left < right:
            water = (right - left) * min(heights[left], heights[right])
            max_result = max(max_result, water)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return max_result
        