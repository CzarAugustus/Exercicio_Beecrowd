class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u]) 
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal_mst(n, edges):
    uf = UnionFind(n)
    mst_cost = 0
    edges.sort(key=lambda x: x[2])

    for u, v, cost in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_cost += cost

    return mst_cost


def main():
    while True:
        m, n = map(int, input().split())
        if m == 0 and n == 0:
            break

        edges = []
        total_cost = 0

        for _ in range(n):
            x, y, z = map(int, input().split())
            edges.append((x, y, z))
            total_cost += z

        mst_cost = kruskal_mst(m, edges)
        
        savings = total_cost - mst_cost
        print(savings)


if __name__ == "__main__":
    main()
