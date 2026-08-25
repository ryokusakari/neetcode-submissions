class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, res = [], [0]*len(temperatures)
        current_max = 0

        for day, temp in enumerate(reversed(temperatures)):
            if temp >= current_max:
                stack = [(temp, day)]
                res[-(day+1)] = 0
                current_max = temp
            else:
                while temp >= stack[-1][0]:
                    stack.pop()
                res[-(day+1)] = day - stack[-1][1]
                stack.append((temp, day))
                
        
        return res
                

            

