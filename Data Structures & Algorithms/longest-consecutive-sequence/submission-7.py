class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        thisSet = set(nums)
        longest = 0

        for num in nums:
            length = 1
            while (num + length) in thisSet:
                length += 1
            longest = max(length, longest)
        
        return longest

                
        