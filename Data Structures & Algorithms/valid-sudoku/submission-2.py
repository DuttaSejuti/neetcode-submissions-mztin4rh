class Solution:
    # TC: O(n^2), SC: O(1) => 3 pass
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     dummy_list = [0]*10

    #     # row inspection
    #     for r in range(0,9):
    #         dummy_list = [0]*10
    #         for c in range(0,9):
    #             if board[r][c] == '.':
    #                 continue
    #             element = int(board[r][c])
    #             if dummy_list[element] == 1:
    #                 return False
    #             dummy_list[element] = 1
        
    #     #col inspection
    #     for c in range(0,9):
    #         dummy_list = [0]*10
    #         for r in range(0,9):
    #             if board[r][c] == '.':
    #                 continue
    #             element = int(board[r][c])
    #             if dummy_list[element] == 1:
    #                 return False
    #             dummy_list[element] = 1
        
    #     # 3*3 box inspection
    #     for r in range(0, 9 ,3):
    #         for c in range(0, 9, 3):
    #             dummy_list = [0]*10
    #             for i in range(0,3):
    #                 for j in range(0,3):
    #                     if board[r+i][c+j] == '.':
    #                         continue
    #                     element = int(board[r+i][c+j])
    #                     if dummy_list[element] == 1:
    #                         return False
    #                     dummy_list[element] = 1
            
    #     return True


    # TC: O(n^2) SC:O(n^2) => 1 pass
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        square = defaultdict(set) # considering each 3*3 square from 0 indexed

        for r in range(0,9):
            for c in range(0,9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in row_map[r] or
                    board[r][c] in col_map[c] or
                    board[r][c] in square[(r//3, c//3)]):
                    return False
                
                row_map[r].add(board[r][c])
                col_map[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
        return True

