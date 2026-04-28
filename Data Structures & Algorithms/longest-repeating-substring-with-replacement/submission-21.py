class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        maxf = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1 # update the counts
            maxf = max(maxf, count[s[r]]) # max freqeuncy
            while r - l + 1 - maxf > k: # len - maxf
                count[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        
        return res
