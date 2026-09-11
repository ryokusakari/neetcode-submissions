class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        reference = [0]*26
        window = [0]*26
        l,r = 0,0

        for s in s1:
            reference[ord(s) - ord("a")] += 1

        while r < len(s2):
            while r < len(s1)-1:
                window[ord(s2[r]) - ord("a")] += 1
                r += 1

            window[ord(s2[r]) - ord("a")] += 1
            if window == reference:
                return True
            
            window[ord(s2[l]) - ord("a")] -= 1
            l += 1
            r += 1
        
        return False


        