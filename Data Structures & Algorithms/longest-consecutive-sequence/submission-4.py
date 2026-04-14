class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        thisSet = set(nums)
        longest = 0

        for num in nums:
            length = 1
            if (num + 1) in thisSet:
                length += 1
                num += 1
                while (num + 1) in thisSet:
                    length += 1
                    num += 1
            longest = max(length, longest)
        
        return longest

                
        