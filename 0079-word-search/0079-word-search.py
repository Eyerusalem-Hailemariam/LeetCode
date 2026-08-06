class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        row, col = len(board), len(board[0])

        board_count = {}

        for r in range(row):
            for c in range(col):
                char = board[r][c]
                board_count[char] = board_count.get(char, 0) + 1
        word_count = {}

        for char in word:
            word_count[char] = word_count.get(char, 0) + 1
        
        for char, count in word_count.items():
            if board_count.get(char, 0) < count:
                return False
            
        

        
        def  backtrack(r, c, index):
            if index  == len(word):
                return True
            
            if (c < 0 or c >= col or
                r < 0 or r >= row or board[r][c] != word[index]):
                return False

            temp = board[r][c]
            board[r][c] = "#"
            found = (backtrack(r + 1, c, index + 1) or
                    backtrack(r, c + 1, index + 1) or
                    backtrack(r - 1, c, index + 1) or
                    backtrack(r , c - 1, index + 1))
            
            board[r][c] = temp

            return found

        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True
        return False  

    