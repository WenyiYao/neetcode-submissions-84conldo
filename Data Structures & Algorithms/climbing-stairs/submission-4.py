class Solution:
    def climbStairs(self, n: int) -> int:
        two, one = 1, 1

        for i in range(n - 1):
            temp = one # [k-1]
            one = one + two #[k] -> [k - 1]
            two = temp #下一步的[k-2]
        
        return one
        
        