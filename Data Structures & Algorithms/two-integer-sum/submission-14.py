class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            # check if the complement exists
            if complement in hashmap.keys():
                # return the complement and current
                return [hashmap[complement],i]
            else:
                # adding the current
                hashmap[nums[i]] = i
        