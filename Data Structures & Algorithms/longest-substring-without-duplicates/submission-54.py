class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        mp = {}
        longest = 0

        for i,r in enumerate(s):
            if r in mp:
                l = max(l, mp[r] + 1)
            mp[r] = i # key: r, value: index
            longest = max(longest, i - l + 1)

        return longest