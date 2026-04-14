class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        resIndex = 0
        resLen = 0
        
        for i in range(len(s)):
            # odd
            l, r = i,i # mid
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if resLen < (r - l + 1):
                    resLen = r - l + 1
                    resIndex = l
                l -= 1
                r += 1
            
            # even
            l, r = i, i + 1 # mid
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if resLen < (r - l + 1):
                    resLen = r - l + 1
                    resIndex = l  
                l -= 1
                r += 1
        
        return s[resIndex:resIndex + resLen]