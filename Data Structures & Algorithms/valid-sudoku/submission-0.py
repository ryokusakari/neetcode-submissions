class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        memory = {str(x):{"i":[],"j":[],"s":[]} for x in range(1,10)}
        for i in range(9):
            for j in range(9):
                s = str(int(math.ceil((i+1)/3))) + str(int(math.ceil((j+1)/3)))
                if board[i][j].isnumeric():
                    mem = memory[board[i][j]]
                    if i in mem["i"] or j in mem["j"] or s in mem["s"]:
                        return False
                    else:
                        memory[board[i][j]]["i"].append(i)
                        memory[board[i][j]]["j"].append(j)
                        memory[board[i][j]]["s"].append(s)
        return True

        