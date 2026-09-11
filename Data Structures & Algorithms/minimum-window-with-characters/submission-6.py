class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        character_map = {}

        for character in t:
            character_map[character] = character_map.get(character, 0) - 1
        
        min_length = float("inf")
        result = ""
        l,r = 0,0

        while r < len(s):
            while min(character_map.values()) < 0:
                if r == len(s):
                    return result
                elif s[r] in character_map:
                    character_map[s[r]] += 1
                r += 1

            while min(character_map.values()) >= 0:
                if s[l] in character_map:
                    character_map[s[l]] -= 1
                l += 1
                
            if r-l+1 < min_length: 
                min_length = r-l+1
                result = s[l-1:r]
        
        return result
            

        

            


