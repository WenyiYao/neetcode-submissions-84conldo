class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            # make key with character
            # alphabet sort
            key = tuple(sorted(string))
            if key in anagrams:
                anagrams[key].append(string)
            else: 
                anagrams[key].append(string)

        return anagrams.values()