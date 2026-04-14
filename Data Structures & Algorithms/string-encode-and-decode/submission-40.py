class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            length = len(string)
            encoded = encoded + str(length) + "#" + string
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            string = str(s[j+1:j+length+1])
            res.append(string)
            i = j+length+1 
        return res


    