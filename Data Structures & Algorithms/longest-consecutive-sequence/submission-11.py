class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        set_nums = set(nums)
        sequences = collections.defaultdict(set)
        for n in nums:
            if n - 1 in set_nums:
                continue
            else:
                sequences[n].add(n)
                next_num = n + 1
                while next_num in set_nums:
                    sequences[n].add(next_num)
                    next_num += 1
            
        max_sequences = len(sequences[nums[0]])
        for key in sequences:
            if len(sequences[key]) > max_sequences:
                max_sequences = len(sequences[key])
        
        return max_sequences

        