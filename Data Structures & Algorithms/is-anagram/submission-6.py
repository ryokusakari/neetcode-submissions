class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        characters = [0]*26
        for i in range(len(s)):
            characters[ord(s[i]) - ord("a")] += 1
            characters[ord(t[i]) - ord("a")] -= 1

        for count in characters:
            if count != 0:
                return False
        
        return True

