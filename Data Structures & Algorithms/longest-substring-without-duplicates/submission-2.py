class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, maximum = 0,0,0

        while j<len(s):
            j += 1
            while len(s[i:j+1]) != len(set(s[i:j+1])):
                i += 1
            maximum = max(maximum, len(s[i:j+1]))
        
        return maximum
                

            
