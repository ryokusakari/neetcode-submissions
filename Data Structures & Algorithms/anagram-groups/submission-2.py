class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_memory = {}
        characters_count = [0]*26

        for string in strs:
            for s in string: 
                characters_count[ord(s) - ord("a")] += 1

            anagram_id = str(characters_count)

            if anagram_id not in anagrams_memory:
                anagrams_memory[anagram_id] = [string]
            else:
                anagrams_memory[anagram_id].append(string)
            
            characters_count = [0]*26

        return list(anagrams_memory.values())
            
