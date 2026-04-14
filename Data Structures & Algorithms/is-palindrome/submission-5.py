class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(filter(str.isalnum, s))
        reverse = s[::-1]
        

        for index in range(len(s)):
            if (s[index] != reverse[index]):
                return False

        return True
        