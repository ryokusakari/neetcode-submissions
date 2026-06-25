class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + "#" + string
        return result

    def decode(self, s: str) -> List[str]:
        result, i, string_length = [], 0, ""
        while i < len(s):
            if s[i] == "#":
                if int(string_length) == 0:
                    result.append("")
                else:
                    result.append(s[i+1:i+1+int(string_length)])
                i += 1 + int(string_length)
                string_length = ""
            else:
                string_length += s[i]
                i += 1
                
        return result




