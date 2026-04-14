class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        res = 0
        count = {}

        while r < len(s):
            if s[r] in count:
                l = max(count[s[r]] + 1,l)
            count[s[r]] = r
            res = max(r - l + 1,res)
            r += 1

        return res