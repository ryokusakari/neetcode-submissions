class Solution:
    def isValid(self, s: str) -> bool:
        memory = ["_"]
        for char in s:
            match char:
                case "(":
                    memory.append(")")
                case "{":
                    memory.append("}")
                case "[":
                    memory.append("]")
                case _:
                    if memory[-1] == char:
                        memory.pop()
                    else:
                        return False
    
        return memory == ["_"] 
