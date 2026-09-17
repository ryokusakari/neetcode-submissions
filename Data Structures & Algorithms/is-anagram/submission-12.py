class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            map = [0]*26
            for i in range(len(s)):
                map[ord(s[i]) - ord("a")] += 1
                map[ord(t[i]) - ord("a")] -= 1
            return all(char == 0 for char in map)
                