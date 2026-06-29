class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True

        s = s.lower()
        i,j = 0, len(s) - 1
        while j > i:
            if not s[i].isalnum() or not s[j].isalnum():
                if not s[i].isalnum():
                    i += 1
                    continue
                if not s[j].isalnum():
                    j -= 1
                    continue
            elif s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True

                



        