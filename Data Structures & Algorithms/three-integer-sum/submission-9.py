class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sum3 = 0
        result = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    sum3 = nums[i] + nums[j] + nums[k]
                    if sum3 == 0:
                        li = [nums[i],nums[j],nums[k]]
                        if li not in result:
                            result.append(li)

        return result