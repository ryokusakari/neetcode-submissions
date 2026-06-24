class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i, length = [], 0, ""
        while i < len(s):
            length += s[i]
            i += 1
            if s[i] == "#":
                new = ""
                i += 1
                for x in range(int(length)):
                    new += s[i]
                    i += 1
                res.append(new)
                length = ""
        return res

            

