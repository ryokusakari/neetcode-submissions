class Solution:

    def encode(self, strs: List[str]) -> str:
        coded = ""
        for string in strs:
            coded += str(len(string)) + "#" + string
        return coded


    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        decoded = []
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            i += 1
            decoded.append(s[i:i+int(length)])
            i += int(length)
        return decoded

            



