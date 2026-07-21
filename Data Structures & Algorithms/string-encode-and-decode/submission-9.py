class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""

        result = []
        for string in strs:
            result.append(str(len(string)) + "#" + string)
        return "".join(result)



    def decode(self, s: str) -> List[str]:
        result = []
        counter, i = "",0
        while i < len(s):
            if s[i] == "#":
                result.append(s[i+1:i+1+int(counter)])
                i += 1 + int(counter)
                counter = ""
            else:
                counter += s[i]
                i += 1

        return result



