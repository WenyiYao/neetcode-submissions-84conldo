class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        count2 = {}

        for s in range(len(s1)):
            count1[s1[s]] = count1.get(s1[s], 0) + 1
        
        curr = 0
        need = len(count1)
        res = False
        for i in range(len(s2)):
            if i + len(s1) - 1 >= len(s2):
                break

            curr = 0
            count2 = {}

            for j in range(i, i + len(s1)):
                count2[s2[j]] = count2.get(s2[j], 0) + 1
                if s2[j] in count1:
                    if count2[s2[j]] == count1[s2[j]]:
                        curr += 1
                    if count2[s2[j]] > count1[s2[j]]:
                        break
                else:
                    break
                if curr == need:
                    return True
        
        return res
        