class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            code = [0]*26
            for character in string: 
                code[ord(character) - ord("a")] += 1
            anagrams[tuple(code)].append(string)
        
        return list(anagrams.values())
            