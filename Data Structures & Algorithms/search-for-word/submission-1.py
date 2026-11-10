class Solution(object):
    def exist(self, board, word):

        row = len(board)
        col = len(board[0])


        def dfs ( r , c , index):
            if index == len(word):
                return True
            
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] != word[index]:
                return False
            
            temp = board[r][c]
            board[r][c] = "#"

            result = ( dfs( r+1, c, index + 1 ) or
                    dfs( r-1, c, index + 1 ) or
                    dfs( r, c+1, index + 1 ) or
                    dfs( r, c-1, index + 1 )  )

            board[r][c] = temp

            return result

        for i in range (row):
            for j in range (col):
                if board[i][j] == word[0] and dfs(i , j, 0):
                    return True
        
        return False