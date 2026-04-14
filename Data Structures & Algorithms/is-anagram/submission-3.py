class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge cases
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False

        s_dict = {}
        t_dict = {}

        for s_char in s:
            if s_char in s_dict:
                s_dict[s_char] = s_dict[s_char] + 1
            else:
                s_dict[s_char] = 0
        
        for t_char in t:
            if t_char in t_dict:
                t_dict[t_char] += 1
            else:
                t_dict[t_char] = 0
        
        for s_char in s_dict:
            if s_char not in t_dict:
                return False
            if s_dict[s_char] != t_dict[s_char]:
                return False
        
        return True
            
            
        
        