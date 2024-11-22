class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Caminho compressão
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            # União por rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(num_routers, edges):
    # Ordena todas as arestas pelo custo P
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(num_routers)
    
    mst_cost = 0
    edges_used = 0
    
    for v, w, p in edges:
        # Verifica se adicionar essa aresta formará um ciclo
        if uf.find(v) != uf.find(w):
            uf.union(v, w)
            mst_cost += p
            edges_used += 1
            
            # Se usamos R - 1 arestas, já temos a árvore geradora mínima completa
            if edges_used == num_routers - 1:
                break
                
    return mst_cost

# Entrada de dados
R, C = map(int, input().split())
edges = []

for _ in range(C):
    V, W, P = map(int, input().split())
    edges.append((V - 1, W - 1, P))  # Ajusta os índices para 0-baseados

# Calcula e imprime o custo total da árvore geradora mínima
print(kruskal(R, edges))
