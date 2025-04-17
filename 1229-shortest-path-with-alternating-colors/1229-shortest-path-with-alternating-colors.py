class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_adj = defaultdict(list)
        blue_adj = defaultdict(list)

        for u, v in redEdges:
            red_adj[u].append(v)
        for u, v in blueEdges:
            blue_adj[u].append(v)

        distances = [[-1] * n for _ in range(2)] 
        distances[0][0] = distances[1][0] = 0

        q = deque()
        q.append((0, 0))
        q.append((0, 1))  

        while q:
            node, color = q.popleft()
            next_color = 1 - color 
            neighbors = blue_adj[node] if color == 0 else red_adj[node]

            for neighbor in neighbors:
                if distances[next_color][neighbor] == -1:
                    distances[next_color][neighbor] = distances[color][node] + 1
                    q.append((neighbor, next_color))

        result = []
        for red_dist, blue_dist in zip(distances[0], distances[1]):
            if red_dist == -1 or blue_dist == -1:
                result.append(max(red_dist, blue_dist))
            else:
                result.append(min(red_dist, blue_dist))

        return result


            