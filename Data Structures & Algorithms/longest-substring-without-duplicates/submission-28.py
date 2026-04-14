class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, res = 0,0,0
        mp = {}

        while r < len(s):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(r - l + 1, res)
            r += 1

        return res