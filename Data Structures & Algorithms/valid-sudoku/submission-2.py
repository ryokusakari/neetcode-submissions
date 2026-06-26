class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_memory = defaultdict(set)
        column_memory = defaultdict(set)
        subbox_memory = defaultdict(set)

        for row in range(9):
            for column in range(9):
                number = board[row][column]
                if number == ".":
                    continue
                if (number in row_memory[row]
                    or number in column_memory[column]
                    or number in subbox_memory[(row//3, column//3)]):
                    return False
                
                column_memory[column].add(number)
                row_memory[row].add(number)
                subbox_memory[(row//3, column//3)].add(number)

        print(column_memory)
        print(row_memory)
        print(subbox_memory)
        return True


