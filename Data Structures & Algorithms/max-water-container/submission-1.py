class Solution:
    def maxArea(self, heights: List[int]) -> int:
        fwd, rev, most = 0, len(heights)-1, 0
        while rev>fwd:
            vol = (rev-fwd)*min(heights[rev], heights[fwd])
            if vol > most:
                most = vol
            if heights[rev] <= heights[fwd]:
                rev -= 1
            else:
                fwd += 1
            
        return most
            


        