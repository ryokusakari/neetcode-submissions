class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for character in tokens:
            if character not in ["+","-","*","/"]:
                stack.append(int(character))
            else:
                b = stack.pop()
                a = stack.pop()
                match character:
                    case "+":
                        stack.append(a+b)
                    case "-":
                        stack.append(a-b)
                    case "*":
                        stack.append(a*b)
                    case "/":
                        stack.append(math.trunc(a/b))

        return stack.pop()
                
