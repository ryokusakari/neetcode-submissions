class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1

        l,r = 0,1
        maximum = 0
        character_map = defaultdict(int)

        character_map[s[l]] = 1

        while r < len(s):
            character_map[s[r]] = character_map.get(s[r],0) + 1
            replacement = sum(character_map.values()) - max(character_map.values())
            while replacement > k: 
                character_map[s[l]] -= 1
                l += 1
                replacement = sum(character_map.values()) - max(character_map.values())
            maximum = max(maximum, r-l+1)
            r += 1

        return maximum
            
            


            

            