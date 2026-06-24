class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Initialise pointers at back and front
        #Iterate through characters until fwd > rev
        #If any characters are not the same, return false
        #If the character is not alphanumeric, skip

        if len(s) <= 1:
            return True

        s = s.lower()
        fwd, rev = 0,len(s)-1
        while fwd < rev:
            if s[fwd].isalnum() and s[rev].isalnum():
                if s[fwd] == s[rev]:
                    fwd += 1
                    rev -= 1
                    continue
                else:
                    return False
            else:
                if not s[fwd].isalnum():
                    fwd += 1
                if not s[rev].isalnum():
                    rev -= 1
        return True
                    


        