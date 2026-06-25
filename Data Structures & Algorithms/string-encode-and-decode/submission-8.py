class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for string in strs:
            result.append(f"{len(string):4}" + string)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        while i < len(s):
            j = i + 4
            length = int(s[i:j])
            result.append(s[j:j+length])
            i = j + length          
        return result


            
