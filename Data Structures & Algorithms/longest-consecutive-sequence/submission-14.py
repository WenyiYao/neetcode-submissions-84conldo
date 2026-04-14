class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        
        for n in set_nums:
            if n - 1 not in set_nums:
                length = 1
                next_num = n + 1
                while next_num in set_nums:
                    length += 1
                    next_num += 1
                longest = max(length,longest)
        
        return longest

        