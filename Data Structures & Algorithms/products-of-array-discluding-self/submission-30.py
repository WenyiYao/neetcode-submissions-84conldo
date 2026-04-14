class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = {}
        postfix = {}
        res = []

        prefix[0] = 1
        postfix[len(nums) - 1] = 1
        res.append(1)

        for i in range(1, len(nums), 1):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            res.append(prefix[i])
        
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
            res[i] = res[i] * postfix[i]
        
        return res

