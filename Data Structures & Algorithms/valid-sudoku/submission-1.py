class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_memory = defaultdict(list)
        subbox_memory = defaultdict(list)

        column, row = 0,0
        while row < 9:
            row_memory = [0]*9
            while column < 9:
                number = board[row][column]
                subbox = column//3 + row//3*3

                if number.isnumeric():
                    if row_memory[int(number)-1] != 0:
                        return False
                    elif number in column_memory[column] or number in subbox_memory[subbox]:
                        print(column_memory)
                        print(subbox_memory)
                        return False
                    else:
                        column_memory[column].append(number)
                        subbox_memory[subbox].append(number)
                        row_memory[int(number)-1] += 1
                column += 1
            row += 1
            column = 0
        
        return True


