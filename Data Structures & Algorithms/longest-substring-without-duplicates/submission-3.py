class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        character_map = {}
        l,result = 0,0

        for r in range(len(s)):
            if s[r] in character_map: 
                l = max(character_map[s[r]]+1, l)
            character_map[s[r]] = r
            result = max(result, r-l+1)
        
        return result

        