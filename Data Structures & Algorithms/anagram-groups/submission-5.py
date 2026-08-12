class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for string in strs:
            code_list = [0]*26
            for s in string: 
                code_list[ord(s) - ord("a")] += 1
            code = tuple(code_list)
            anagram_groups[code].append(string)
        
        return list(anagram_groups.values())

