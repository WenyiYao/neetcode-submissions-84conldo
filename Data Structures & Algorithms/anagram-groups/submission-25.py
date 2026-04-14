class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            # make string key
            keys = tuple(sorted(string))
            # anagrams share the same key automatically
            # just append the string
            anagrams[keys].append(string)

        return anagrams.values()