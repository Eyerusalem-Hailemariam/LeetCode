class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outgoing = [0 for i in range(len(graph))]
        reversed_graph = [[] for i in range(len(graph))]
        queue = deque()
        res = []
        for u in range(len(graph)):
            outgoing[u] = len(graph[u])
            for v in graph[u]:
                reversed_graph[v].append(u)
                
        for i in range(len(graph)):
            if outgoing[i] == 0:
                queue.append(i)

        while queue:
            safegraph = queue.popleft()
            res.append(safegraph)
            for neigh in reversed_graph[safegraph]:
                outgoing[neigh] -= 1

                if outgoing[neigh] == 0:
                    queue.append(neigh)
         

        return  sorted(res)