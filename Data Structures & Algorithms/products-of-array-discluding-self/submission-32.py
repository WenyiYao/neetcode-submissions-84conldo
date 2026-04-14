class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sums = 1
        results = [0] * len(nums)
        zero_count = 0
        zero_position = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
                zero_position = i
    

        if zero_count == 1:
            for num in nums:
                if num != 0:
                    sums = sums * num
            results[zero_position] = sums
        else:
            for num in nums:
                sums = sums * num

            for i in range(len(nums)):
                if nums[i] != 0:
                    results[i] = int(sums / nums[i])

        return results
        
        


        





