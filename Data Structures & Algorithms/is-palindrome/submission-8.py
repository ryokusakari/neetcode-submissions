class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1

        s = s.lower()
        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            elif not s[l].isalnum():
                l += 1
            else:
                r -= 1
        
        return True

                
            