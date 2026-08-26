class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for s in strs:
            output.append(str(len(s)))
            output.append("#")
            output.append(s)
        return "".join(output)


    def decode(self, s: str) -> List[str]:
        l, r = 0,1
        output = []
        while r <= (len(s)-1):
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            l = r + 1
            r = l + length

            if length == 0:
                output.append("")
            else:
                output.append(s[l:r])
            l = r
        
        return output
        

            
            
            


