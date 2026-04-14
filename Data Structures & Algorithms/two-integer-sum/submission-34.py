class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {} #value -> index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in pair:
                return [pair[diff], i]
            pair[n] = i
            
        

        