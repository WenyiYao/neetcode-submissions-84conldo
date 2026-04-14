class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = {}
        postfix = {}
        
        pre_value = 1
        prefix[0] = 1
        for i in range(1, len(nums), 1):
            pre_value = pre_value * nums[i - 1]
            prefix[i] = pre_value

        post_value = 1
        postfix[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            post_value = post_value * nums[i + 1]
            postfix[i] = post_value

        li = []
        for i in range(0, len(nums), 1):
            li.append(prefix[i] * postfix[i])
        
        return li
        
