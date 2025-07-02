class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key = lambda t : t[0])

        res, heap = [], []
        i, time = 0, 0

        while heap or i < len(tasks):
            if not heap and time < tasks[i][0]:
                    time = tasks[i][0]
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1

            if heap:
                procTime, index = heapq.heappop(heap)
                time += procTime
                res.append(index)
        return res


       
        