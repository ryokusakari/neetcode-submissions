class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        result = [0]*26

        for i in range(len(s)):
            result[ord(s[i]) - ord("a")] += 1
            result[ord(t[i]) - ord("a")] -= 1

        for bit in result: 
            if bit != 0:
                return False
        return True

     
