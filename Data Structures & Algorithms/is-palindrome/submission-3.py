class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Iterate through list from front and back
        #If the character is not alphanumeric, skip
        #If the characters are not equal, return false
        #If the characters are equal from start to end, return true

        s = s.lower()
        fwd,rev = 0,-1
        while -1*rev + fwd < len(s):
            if s[fwd].isalnum() and s[rev].isalnum():
                if s[fwd] != s[rev]:
                    return False
                fwd += 1
                rev -= 1
            if not s[fwd].isalnum():
                fwd += 1
            if not s[rev].isalnum():
                rev -= 1
        return True

        