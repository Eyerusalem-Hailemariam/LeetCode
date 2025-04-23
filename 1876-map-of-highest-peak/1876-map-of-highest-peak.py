class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n, m = len(isWater), len(isWater[0])
        visited = [[-1] * m  for i in range(n)] 
        queue = deque()
        for i in range(len(isWater)):
            for j in range(len(isWater[i])):
                if isWater[i][j] == 1:
                    queue.append([i, j])
                    visited[i][j] = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()

            for dx, dy in directions:
                new_row, new_col = dx + row, dy + col
                if 0 <= new_row < n and 0 <= new_col < m and visited[new_row][new_col] == -1:
                    visited[new_row][new_col] = visited[row][col] + 1
                    queue.append((new_row, new_col))
        return visited


