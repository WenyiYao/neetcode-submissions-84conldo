class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_i_2, rob_i_1 = 0,0
        for num in nums:
            currMax = max(rob_i_1, rob_i_2 + num)
            rob_i_2 = rob_i_1
            rob_i_1 = currMax
            
        return rob_i_1
            

        
        return maxSum