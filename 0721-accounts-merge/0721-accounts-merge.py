class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, X):
        if X == self.root[X]:
            return self.root[X]
        self.root[X] = self.find(self.root[X])
        return self.root[X]

    def union(self, X, Y):
        rootX, rootY = self.find(X), self.find(Y)
        if rootX != rootY:
            rankX = self.rank[rootX]
            rankY = self.rank[rootY]
            if rankX > rankY:
                self.root[rootY] = rootX
            elif rankX < rankY:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        u_f = UnionFind(len(accounts))
        emailtoAccount = {}

        for i, account in enumerate(accounts):
            for j in account[1:]:
                if j in emailtoAccount:
                    u_f.union(i, emailtoAccount[j])
                else:
                    emailtoAccount[j] = i
        emailGroup = defaultdict(list)
        for e, i in emailtoAccount.items():
            leader = u_f.find(i)
            emailGroup[leader].append(e)
        
        res = []
        for i, email in emailGroup.items():
            name = accounts[i][0]
            res.append(([name] + sorted(emailGroup[i])))
        return res

        