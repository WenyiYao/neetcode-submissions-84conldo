class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i,num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            complement = 0 - num
            index1 = i + 1
            index2 = len(nums) - 1
            while index1 < index2:
                if nums[index1] + nums[index2] == complement:
                    result.append([num, nums[index1], nums[index2]])
                    index1 += 1
                    index2 -= 1
                    while index1 < index2 and nums[index2] == nums[index2 + 1]:
                        index2 -= 1
                    while index1 < index2 and nums[index1] == nums[index1 - 1]:
                        index1 += 1
                elif nums[index1] + nums[index2] < complement:
                    index1 += 1
                else:
                    index2 -= 1
        
        return result

        