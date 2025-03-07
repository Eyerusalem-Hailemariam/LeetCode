class RecentCounter:

    def __init__(self):
        self.count = 0
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
                self.q.popleft()
        
        self.count = len(self.q)
      
        return self.count


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)