import collections
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hmap = collections.defaultdict(list)
        for u, v in edges:
            hmap[u].append(v)
            hmap[v].append(u)
        count = 0
        visited = set()
        
        def dfs(node, hmap, visited):
            if node in hmap:
                for neighbor in hmap[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        dfs(neighbor, hmap, visited)
        for node in range(n):
            if node not in visited:
                dfs(node, hmap, visited)
                count +=1
        return count
            
        
