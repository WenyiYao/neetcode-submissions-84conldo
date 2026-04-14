class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # list for 2 string
        mp1, mp2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            # reference
            mp1[ord(s1[i]) - ord('a')] += 1
            # slidng window
            mp2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        # first round
        for i in range(len(mp1)):
            if mp1[i] == mp2[i]:
                matches += 1
        
        # next
        l = 0
        r = len(s1)
        while r < len(s2):
            if matches == 26:
                return True

            # move to right
            index = ord(s2[r]) - ord('a')
            mp2[index] += 1
            if mp2[index] == mp1[index]:
                matches += 1
            elif mp2[index] - 1 ==  mp1[index]:
                matches -= 1
            r += 1

            # delete the left one
            index = ord(s2[l]) - ord('a')
            mp2[index] -= 1
            if mp2[index] == mp1[index]:
                matches += 1
            elif mp2[index] + 1 == mp1[index]:
                matches -= 1
            l += 1

        return matches == 26


