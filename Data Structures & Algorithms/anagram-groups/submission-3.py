class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_memory = defaultdict(list)

        for string in strs:
            characters_count = [0]*26
            for character in string: 
                characters_count[ord(character) - ord("a")] += 1

            anagrams_memory[tuple(characters_count)].append(string)

        return list(anagrams_memory.values())
            
