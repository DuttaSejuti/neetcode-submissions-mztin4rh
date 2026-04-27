class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result = True
        dummy_list = [0]*10
        row_map = dict()
        col_map = dict()

        # row inspection
        for r in range(0,9):
            dummy_list = [0]*10
            for c in range(0,9):
                if board[r][c] == '.':
                    continue
                element = int(board[r][c])
                if dummy_list[element] == 1:
                    return False
                dummy_list[element] = 1
            row_map[r] = 1
        
        #col inspection
        for c in range(0,9):
            dummy_list = [0]*10
            for r in range(0,9):
                if board[r][c] == '.':
                    continue
                element = int(board[r][c])
                if dummy_list[element] == 1:
                    return False
                dummy_list[element] = 1
            col_map[c] = 1
        
        # 3*3 box inspection
        for r in range(0, 9 ,3):
            for c in range(0, 9, 3):
                dummy_list = [0]*10
                for i in range(0,3):
                    for j in range(0,3):
                        if board[r+i][c+j] == '.':
                            continue
                        element = int(board[r+i][c+j])
                        if dummy_list[element] == 1:
                            return False
                        dummy_list[element] = 1
            
        return result