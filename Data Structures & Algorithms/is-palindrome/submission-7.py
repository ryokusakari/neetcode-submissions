class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l,r = 0,len(s)-1

        while l<r:
            if s[l].isalnum() and s[r].isalnum() and s[r] != s[l]:
                return False
            elif not s[l].isalnum() and not s[r].isalnum():
                l += 1
                r -= 1
            elif not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                l += 1
                r -= 1
        
        return True
                

