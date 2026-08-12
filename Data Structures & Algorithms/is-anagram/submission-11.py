class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        character_map = [0]*26

        for i in range(len(s)): 
            character_map[ord(s[i]) - ord("a")] += 1
            character_map[ord(t[i]) - ord("a")] -= 1

        for val in character_map:
            if val != 0:
                return False
        return True