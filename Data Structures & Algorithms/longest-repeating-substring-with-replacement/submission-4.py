class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = [0]*26
        current_length, max_length = 0,0
        l = 0

        for char in s:
            window[ord(char) - ord("A")] += 1
            current_length += 1

            while sum(window) - max(window) > k:
                window[ord(s[l]) - ord("A")] -= 1
                current_length -= 1
                l += 1
            
            max_length = max(max_length, current_length)
        
        return max_length
            
