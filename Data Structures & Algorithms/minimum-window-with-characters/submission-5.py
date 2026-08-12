class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        character_map = [0]*(ord("z") - ord("A") + 1)

        for character in t: 
            character_map[ord(character) - ord("A")] -= 1

        result, minimum, l = [0,0], len(s)+1, 0
       
        for r in range(len(s)):
            character_map[ord(s[r]) - ord("A")] += 1
            while all(count >= 0 for count in character_map):
                if r-l+1 < minimum:
                    result = [l,r+1]
                    minimum = r-l+1
                character_map[ord(s[l]) - ord("A")] -= 1
                l += 1

        return s[result[0]: result[1]]

        
            
