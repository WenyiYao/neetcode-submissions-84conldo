class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one # [k-2]
            one = one + two #[k]
            two = temp #[k-1]
        
        return one
        
        