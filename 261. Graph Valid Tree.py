import collections
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False
        hmap = collections.defaultdict(list)
        for u, v in edges:
            hmap[u].append(v)
            hmap[v].append(u)
        visited = [False]*n
        def dfs(curr):
            if visited[curr]:
                return
            visited[curr] = True
            for neighbor in hmap[curr]:
                dfs(neighbor)
    
        dfs(0)
        return False not in visited
