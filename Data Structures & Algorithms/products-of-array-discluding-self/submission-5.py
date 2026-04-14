class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        product = 1
        prefix.append(product)
        for num in nums:
            product = product * num
            prefix.append(product)
        
        product = 1
        postfix.append(product)
        for i in range(len(nums) - 1, -1, -1):
            product = product * nums[i]
            postfix.append(product)

        li = []
        for i in range(len(nums)):
            li.append(prefix[i] * postfix[len(nums)-i-1])
        
        return li

        