class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = {}
        for chara in s:
            if chara in hashmap:
                hashmap[chara] += 1
            else:
                hashmap[chara] = 1
        
        for chara in t:
            if chara in hashmap:
                hashmap[chara] -= 1
            else:
                hashmap[chara] = -1

        for key in hashmap.keys():
            if hashmap[key] != 0:
                return False
        
        return True
        