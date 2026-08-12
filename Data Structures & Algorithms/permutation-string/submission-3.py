class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        map = [0]*26
        map_checker = [0]*26

        for s in s1:
            map[ord(s) - ord("a")] += 1
        
        r,l = 0,0
        while r < len(s1):
            map_checker[ord(s2[r]) - ord("a")] += 1
            r += 1
            
        while r < len(s2):
            if map_checker == map: 
                return True
            else: 
                map_checker[ord(s2[r]) - ord("a")] += 1
                map_checker[ord(s2[l]) - ord("a")] -= 1
                r += 1
                l += 1
        
        if map_checker == map:
            return True 
        else:
            return False
            

            

            