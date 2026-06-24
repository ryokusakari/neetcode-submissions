class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        characters = [0]*26
        characters_copy = characters.copy()
        for i in range(len(s)):
            characters[ord(s[i]) - ord("a")] += 1
            characters[ord(t[i]) - ord("a")] -= 1

        return characters == characters_copy

