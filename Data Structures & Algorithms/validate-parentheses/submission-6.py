class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parens_dict = {"[":"]","{":"}","(":")"}

        for character in s:
            if character in parens_dict:
                stack.append(character)

            elif character in ["]", "}", ")"]:
                if not stack or character != parens_dict[stack.pop()]:
                    return False

        return True if not stack else False

