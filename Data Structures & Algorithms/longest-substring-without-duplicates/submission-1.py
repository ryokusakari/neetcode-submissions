class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #keep track of max length substring
        #move right pointer forward until there is a repeated character
        #update left pointer to right and continue

        maxS,r,l = 0,0,0

        while r < len(s):
            if len(s[l:r+1]) != len(set(s[l:r+1])):
                l +=1
            maxS = max(maxS, r-l+1)
            r += 1
        return maxS

        