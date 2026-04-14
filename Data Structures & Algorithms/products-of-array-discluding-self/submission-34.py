class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        postfix = 1
        res.append(prefix)
        
        for i in range(1, len(nums), 1):
            prefix = prefix * nums[i - 1]
            res.append(prefix)
        
        for i in range(len(nums) - 2, -1, -1):
            postfix = postfix * nums[i + 1]
            res[i] = res[i] * postfix
        
        return res
        
        


        





