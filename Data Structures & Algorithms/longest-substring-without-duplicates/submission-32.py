class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "zxyzxyz"
        # left = 0
        # right = 0
        # biggest = -1
        # substring = ""

        # while left < len(s) and right < len(s):
        #     if s[right] not in substring:
        #         substring = substring + s[right]
        #         right += 1
        #     else:
        #         biggest = max(biggest, right-left)
        #         left += 1
        #         right = left
        #         substring = ""
        # return biggest
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            print(mp)
            res = max(res, r - l + 1)
        return res
        

            

            







        #     if n in s[left:right+1]:e
        #         left += 1
        #     else:
        #         right += 1
        
        # return right - left + 1
