class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        
        board_counts = {}
        for r in range(rows):
            for c in range(cols):
                char = board[r][c]
                board_counts[char] = board_counts.get(char, 0) + 1
                
        word_counts = {}
        for char in word:
            word_counts[char] = word_counts.get(char, 0) + 1
            
        for char, count in word_counts.items():
            if board_counts.get(char, 0) < count:
                return False
       
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]

        def dfs(r, c, index):
   
            if index == len(word):
                return True
            
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                board[r][c] != word[index]):
                return False
            
            temp = board[r][c]
            board[r][c] = '#'
            
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            
            board[r][c] = temp
            
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
                        
        return False