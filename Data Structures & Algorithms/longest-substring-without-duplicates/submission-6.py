#unsure
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        character_set = set()
        max_length = 0
        l = 0

        for r, character in enumerate(s):
            while character in character_set:
                character_set.remove(s[l])
                l += 1
            character_set.add(character)
            max_length = max(max_length, r-l+1)

        return max_length


