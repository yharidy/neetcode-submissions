class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            sorted_str = tuple(sorted(s))
            anagrams.setdefault(sorted_str,[]).append(s)
        return list(anagrams.values())